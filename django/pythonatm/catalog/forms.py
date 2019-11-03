from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
# from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class AccountCreationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    balance = forms.IntegerField()

    # user should not see these and they should be generated for the user
    """
    account_number
    user
    """

class CardCreationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    pin = forms.CharField()

    # user should not see these and they should be generated for the user
    """
    issue_date
    expiration_date
    account
    card_number
    """
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name')
