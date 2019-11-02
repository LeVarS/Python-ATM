from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
# from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    # def save(self, commit=True):
    #     user = User.objects.create_user(
    #         self.cleaned_data['username'],
    #         email=self.cleaned_data['email'],
    #         password=self.cleaned_data['password'],
    #         first_name=self.cleaned_data['first_name'],
    #         last_name=self.cleaned_data['last_name']
    #     )
    #     return user


    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user

# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name')
