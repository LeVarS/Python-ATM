from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from catalog.models import Account, Card, ATMachine, Transaction, ATMachineRefill #, CustomUser
# from catalog.forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'account_number', 'balance') # Inserting "('bank_user')" causes a TypeError
    fields = ['first_name', 'last_name', 'phone_number', ('account_number', 'balance'), 'bank_user']
admin.site.register(Account, AccountAdmin)    # Same thing as "admin.site.register(Account)"

class CardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'account', 'issue_date', 'expiration_date', 'status')
    list_filter = ('issue_date', 'expiration_date', 'status')
    fields = ['first_name', 'last_name', 'phone_number', 'account', ('card_number', 'pin'), ('issue_date', 'expiration_date'), 'status', 'bank_user']
admin.site.register(Card, CardAdmin)

class ATMachineAdmin(admin.ModelAdmin):
    list_display = ('machine_id', 'current_balance', 'last_refill', 'next_maintenance')
    list_filter = ('last_refill', 'next_maintenance')
    fields = ['machine_id', ('current_balance', 'minimum_balance'), ('last_refill', 'next_maintenance')]
admin.site.register(ATMachine, ATMachineAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'type', 'card', 'atm_machine', 'transaction_date', 'status')
    list_filter = ('type', 'card', 'atm_machine', 'transaction_date', 'status')
    fields = ['transaction_id', ('type', 'status'), ('atm_machine', 'card'), ('transaction_date', 'response_code')]
admin.site.register(Transaction, TransactionAdmin)

class ATMachineRefillAdmin(admin.ModelAdmin):
    list_display = ('refill_id', 'refill_amount', 'atm_machine', 'refill_date')
    list_filter = ('atm_machine', 'refill_date')
    fields = [('refill_id', 'refill_amount', 'refill_date'), 'atm_machine']
admin.site.register(ATMachineRefill, ATMachineRefillAdmin)

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username', 'first_name', 'last_name']
# admin.site.register(CustomUser, CustomUserAdmin)
