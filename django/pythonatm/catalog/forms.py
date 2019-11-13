import datetime
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from catalog.models import Account, Card, ATMachine, ATMachineRefill, Transaction
from django.core.validators import MinLengthValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

# from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class AccountCreationForm(ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'address', 'phone_number', 'balance')

class AccountChangeForm(ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'address', 'phone_number')

class CardChangeForm(ModelForm):
    class Meta:
        model = Card
        fields = ('first_name', 'last_name', 'address', 'phone_number', 'pin')

class CardCreationForm(ModelForm):
    account = forms.ModelChoiceField(queryset=Account.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(CardCreationForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.filter(bank_user=user).order_by('account_number')

    def save(self):
        card = super().save(commit=False)
        # card.account = Account.objects.get(account=self.account)
        # card.save()
        return card

    class Meta:
        model = Card
        fields = ('account', 'pin', 'first_name', 'last_name', 'address', 'phone_number')

class CashTransferForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
    receiver = forms.CharField(
        validators=[MinLengthValidator(0)],
        max_length=12,
        help_text='Enter account number for receiving account')
    account = forms.ModelChoiceField(queryset=Account.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(CashTransferForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.filter(bank_user=user).order_by('account_number')
        self.redirect = False

    def transfer_amount(self):
        amount = self.cleaned_data['amount']
        account = self.cleaned_data['account']

        try:
            instance = Account.objects.get(account_number=self.cleaned_data['receiver'])
        except Account.DoesNotExist:
            instance = None

        if amount > account.balance:
            self.redirect = True
            return 1
            #self.message = 'Invalid amount - Receiver account doesn\'t exist'
            # raise ValidationError([
            #     ValidationError(_('Invalid amount - Insufficient Funds in Account'), code="funds"),
            # ])
        elif instance == None:
            self.redirect = True
            return -1
            #self.message = 'Invalid amount - Receiver account doesn\'t exist'
            # raise ValidationError([
            #     ValidationError(_('Invalid amount - Receiver account doesn\'t exist'), code='account'),
            # ])
        else:
            transaction = Transaction()
            transaction.bank_user = account.bank_user
            transaction.description = f"Transfered ${amount} from {account.first_name}'s account to {instance.first_name}'s account"
            transaction.save()
            instance.balance += amount
            account.balance -= amount
            instance.update()
            account.update()
        return amount

class WithdrawTransactionForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
    account = forms.ModelChoiceField(queryset=Account.objects.all())
    atm_machine = forms.ModelChoiceField(queryset=ATMachine.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(WithdrawTransactionForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.filter(bank_user=user).order_by('account_number')
        self.redirect = False

    def withdraw_amount(self):
        amount = self.cleaned_data['amount']
        account = self.cleaned_data['account']
        atm = self.cleaned_data['atm_machine']

        if amount > account.balance:
            self.redirect = True
            return 1
        elif amount > (atm.current_balance - atm.minimum_balance):
            self.redirect = True
            return -1
        else:
            transaction = Transaction()
            transaction.bank_user = account.bank_user
            transaction.description = f"Withdrew ${amount} from {account.first_name}'s account (Account #: {account.account_number})"
            transaction.account = account
            transaction.type = 'W'
            transaction.save()
            atm.current_balance -= amount
            atm.save()
            account.balance -= amount
            account.update()
        return amount

class DepositTransactionForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
    account = forms.ModelChoiceField(queryset=Account.objects.all())
    atm_machine = forms.ModelChoiceField(queryset=ATMachine.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(DepositTransactionForm, self).__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.filter(bank_user=user).order_by('account_number')
        self.redirect = False

    def deposit_amount(self):
        amount = self.cleaned_data['amount']
        account = self.cleaned_data['account']
        atm = self.cleaned_data['atm_machine']

        # if amount > account.balance:
        #     self.redirect = True
        # else:
        transaction = Transaction()
        transaction.bank_user = account.bank_user
        transaction.description = f"Deposited ${amount} into {account.first_name}'s account (Account #: {account.account_number})"
        transaction.account = account
        transaction.type = 'D'
        transaction.save()
        atm.current_balance += amount
        atm.save()
        account.balance += amount
        account.update()
        return amount
    # def save(self):
    #     transaction = super().save(commit=False)
    #     return transaction
    #
    # class Meta:
    #     model = Transaction
    #     fields = ('amount', 'card', 'atm_machine')

# class PhoneChangeForm(ModelForm):
#     phone_number = forms.CharField(
#         #verbose_name='Phone',
#         validators=[MinLengthValidator(10)],
#         max_length=10,
#         help_text='Enter new phone number for Account')
#
#     class Meta:
#         model = Transaction
#         fields = ('atm_machine',)
