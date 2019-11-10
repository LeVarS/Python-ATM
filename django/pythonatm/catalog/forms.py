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

    # user should not see these and they should be generated for the user
    """
    account_number (generated)
    user (generated)
    """

class CardCreationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    pin = forms.CharField()

    # user should not see these and they should be generated for the user
    """
    user (generated)

    issue_date (generated)
    issue_date = forms.DateField(default=timezone.now)

    expiration_date (generated)
    account (generated)
    card_number (generated)
    """

class PhoneChangeForm(ModelForm):
    phone_number = forms.CharField(
        #verbose_name='Phone',
        validators=[MinLengthValidator(10)],
        max_length=10,
        help_text='Enter new phone number for Account')

    class Meta:
        model = Transaction
        fields = ('atm_machine',)

# class PhoneChangeForm(forms.Form):
    #atm_machine = forms.ForeignKey()

    # transaction_date = forms.DateField(default=datetime.date.today())

    # response_code = forms.CharField(default=0)

    # def clean_date(self):
    #     tdate = datetime.date.today()
    #
    #     tdate = self.cleaned_data['tdate']

    # TRANSACTION_TYPE = (
    #     ('PHC', 'Phone Change'),
    #     ('PIC', 'PIN Change'),
    #     ('CHW', 'Cash Withdrawal'),
    #     ('CHT', 'Cash Transfer'),
    #     ('BLE', 'Balance Enquiry')
    # )
    #
    # type = forms.CharField(
    #     max_length=3,
    #     choices=TRANSACTION_TYPE,
    #     blank=True,
    #     default='CHW',
    #     help_text='Tranaction Type')
    #
    # transaction_type = forms.CharField()

    # user should not see these and they should be generated for the user
    """
    user (generated)
    transaction_id (generated)
    transaction_date (generated)
    status (generated)
    card (user should have have choice regrding which card they want to use)
    atm_machine (user should have choice regarding atm location)
    response_code (generated)
    """
