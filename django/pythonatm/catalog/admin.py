from django.contrib import admin
from catalog.models import Account, Card, ATMachine, Transaction

# Register your models here.
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(ATMachine)
admin.site.register(Transaction)
