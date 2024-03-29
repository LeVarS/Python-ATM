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
        elif instance == account:
            self.redirect = True
            return 2
        else:
            transaction_s = Transaction()
            transaction_r = Transaction()
            transaction_s.bank_user = account.bank_user
            transaction_s.account = self.cleaned_data['account']
            transaction_s.type = 'T'
            transaction_s.description = f"Transfered ${amount} from {account.first_name} {account.last_name}'s account (Account #: {account.account_number}) to {instance.first_name} {instance.last_name}'s account (Account #: {account.account_number})."
            transaction_s.save()
            transaction_r.bank_user = Account.objects.get(account_number=self.cleaned_data['receiver']).bank_user
            transaction_r.account = Account.objects.get(account_number=self.cleaned_data['receiver'])
            transaction_r.type = 'T'
            transaction_r.description = f"Received ${amount} from {account.first_name} {account.last_name}'s account."
            transaction_r.save()
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
            transaction.description = f"Withdrew ${amount} from {account.first_name} {account.last_name}'s account (Account #: {account.account_number})."
            transaction.account = self.cleaned_data['account']
            transaction.atm_machine = self.cleaned_data['atm_machine']
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
        if amount > (atm.maximum_balance - atm.current_balance):
            self.redirect = True
        else:
            transaction = Transaction()
            transaction.bank_user = account.bank_user
            transaction.description = f"Deposited ${amount} into {account.first_name} {account.last_name}'s account (Account #: {account.account_number})."
            transaction.account = self.cleaned_data['account']
            transaction.atm_machine = self.cleaned_data['atm_machine']
            transaction.type = 'D'
            transaction.save()
            atm.current_balance += amount
            atm.save()
            account.balance += amount
            account.update()
        return amount
