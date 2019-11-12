import datetime
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from catalog.models import Account, Card, ATMachine, ATMachineRefill, Transaction
from django.core.validators import MinLengthValidator, MinValueValidator

# from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class AccountCreationForm(ModelForm):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number', 'balance')

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
        fields = ('account', 'pin', 'first_name', 'last_name', 'phone_number')

class WithdrawTransactionForm(ModelForm):
    amount = forms.IntegerField(min_value=0)
    card = forms.ModelChoiceField(queryset=Card.objects.all())
    atm_machine = forms.ModelChoiceField(queryset=ATMachine.objects.all())

    def __init__(self, user, *args, **kwargs):
        super(WithdrawTransactionForm, self).__init__(*args, **kwargs)
        self.fields['card'].queryset = Card.objects.filter(bank_user=user).order_by('card_number')

    def save(self):
        transaction = super().save(commit=False)
        return transaction

    class Meta:
        model = Transaction
        fields = ('amount', 'card', 'atm_machine')

class PhoneChangeForm(ModelForm):
    phone_number = forms.CharField(
        #verbose_name='Phone',
        validators=[MinLengthValidator(10)],
        max_length=10,
        help_text='Enter new phone number for Account')

    class Meta:
        model = Transaction
        fields = ('atm_machine',)
