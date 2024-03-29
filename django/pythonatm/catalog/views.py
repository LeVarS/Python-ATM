from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from catalog.models import Account, Card, ATMachine, ATMachineRefill, Transaction
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import CustomUserCreationForm, AccountCreationForm, CardCreationForm, WithdrawTransactionForm, AccountChangeForm, CashTransferForm, DepositTransactionForm, CardChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def index(request):
    """ View function for home page of site. """

    # Generate counts of some fo the main objects
    num_accounts = Account.objects.count()    # same as "Account.objects.all().count()"
    num_cards = Card.objects.count()
    num_atms = ATMachine.objects.count()
    num_transactions = Transaction.objects.count()

    # Available book (status = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_accounts': num_accounts,
        'num_cards': num_cards,
        'num_atms': num_atms,
        'num_transactions': num_transactions,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Bank Members')
            user.groups.add(group)
            user = form.save()
            login(request, user)

            return redirect("index")
        else:
            for msg in form.errors:
                print(form.errors[msg])

    form = CustomUserCreationForm
    context = {
         'form' : form,
    }

    # ../templates/registration/register.html
    return render(request, "register.html", context=context)

def AccountView(request):
    if request.method == "POST":
        #account = Account(bank_user=request.user)
        # form = AccountCreationForm(request.POST, instance=account)
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            account = form.save(commit=False)
            account.bank_user = request.user
            account.save()
            return redirect("my-accounts")
        else:
            for msg in form.errors:
                print(form.errors[msg])

    form = AccountCreationForm
    context = {
         'form' : form,
    }
    return render(request, "catalog/account_creation.html", context=context)

def CardView(request):
    if request.method == "POST":
        #account = Card(bank_user=request.user)
        #form = CardCreationForm(request.POST, instance=account)
        form = CardCreationForm(request.user, request.POST)
        if form.is_valid():
            #form.save()

            card = form.save()
            card.bank_user = request.user
            card.save()
            return redirect("my-cards")
        else:
            for msg in form.errors:
                print(form.errors[msg])

    form = CardCreationForm(request.user)
    context = {
         'form' : form,
    }
    return render(request, "catalog/card_creation.html", context=context)

def CashTransferView(request):
    #instance = Account.objects.get(account_number=pk)
    if request.method == "POST":
        form = CashTransferForm(request.user, request.POST)
        if form.is_valid():
            response_code = form.transfer_amount()
            if form.redirect:
                if response_code == 1:
                    return redirect("insufficient-funds")
                elif response_code == -1:
                    return redirect("nonexistent-account")
                elif response_code == 2:
                    return redirect("transfer-own-account")
            else:
            # form.withdraw_amount()
            #transaction.description = str("Transferred", transaction.amount)
            # transaction.bank_user = request.user
            # transaction.save()
                return redirect("transaction-history")
        else:
            if form.redirect:
                return redirect("insufficient-funds")
                # for error in form.errors.as_data():
                #     if error.code == 'funds':
                #         return redirect("insufficient-funds")
                #     elif error.code == "account":
                #         return redirect("nonexistent-account")

            for msg in form.errors:
                print(form.errors[msg])
    form = CashTransferForm(request.user)
    context = {
         'form' : form,
    }
    return render(request, "catalog/transfer.html", context=context)

def WithdrawTransactionView(request):
    if request.method == "POST":
        form = WithdrawTransactionForm(request.user, request.POST)
        if form.is_valid():
            response_code = form.withdraw_amount()
            if form.redirect:
                if response_code == 1:
                    return redirect("insufficient-funds")
                elif response_code == -1:
                    return redirect("insufficient-atm-funds")
            else:
                return redirect("transaction-history")

        else:
            for msg in form.errors:
                print(form.errors[msg])
    form = WithdrawTransactionForm(request.user)
    context = {
         'form' : form,
    }
    return render(request, "catalog/withdraw.html", context=context)

def DepositTransactionView(request):
    if request.method == "POST":
        form = DepositTransactionForm(request.user, request.POST)
        if form.is_valid():
            form.deposit_amount()
            if form.redirect:
                return redirect("insufficient-atm-capacity")
            else:
                return redirect("transaction-history")
        else:
            for msg in form.errors:
                print(form.errors[msg])
    form = DepositTransactionForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, "catalog/deposit.html", context=context)

def EditAccountView(request, pk):
    instance = Account.objects.get(account_number=pk)
    if request.method == "POST":
        form = AccountChangeForm(request.POST, instance=instance)
        if form.is_valid():
            temp = form.save(commit=False)
            instance.first_name = temp.first_name
            instance.last_name = temp.last_name
            instance.address = temp.address
            instance.phone_number = temp.phone_number
            instance.update()
            return redirect('account-detail', pk)
    form = AccountChangeForm(instance=instance)
    context = {
         'form' : form,
    }
    return render(request, "catalog/edit_account.html", context=context)

def EditCardView(request, pk):
    instance = Card.objects.get(card_number=pk)
    if request.method == "POST":
        form = CardChangeForm(request.POST, instance=instance)
        if form.is_valid():
            temp = form.save(commit=False)
            instance.first_name = temp.first_name
            instance.last_name = temp.last_name
            instance.address = temp.address
            instance.pin = temp.pin
            instance.update()
            return redirect('card-detail', pk)
    form = CardChangeForm(instance=instance)
    context = {
         'form' : form,
    }
    return render(request, "catalog/edit_card.html", context=context)

# def TransactionView(request):
#     form = PhoneChangeForm(request.POST)
#     if form.is_valid():
#         transaction = form.save(commit=False)
#         transaction.bank_user = request.user
#         transaction.save()
#     context = {
#          'form' : form,
#     }
#     return render(request, "phone_change.html", context=context)

def InsufficientFundsView(request):
    """ View function for home page of site. """

    context = {
        'message' : "Not enough funds in sending account!"
    }

    return render(request, 'post_error.html', context=context)

def AccountErrorView(request):
    context = {
        'message' : "Receiving account does not exist!"
    }

    return render(request, 'post_error.html', context=context)

def AtmFundsErrorView(request):
    context = {
        'message' : "ATM Error - Insufficient funds"
    }

    return render(request, 'post_error.html', context=context)

def AtmCapacityErrorView(request):
    context = {
        'message' : "ATM Error - Insufficient capacity"
    }

    return render(request, 'post_error.html', context=context)

def TransferOwnAccountErrorView(request):
    context = {
        'message' : "Unable to transfer to own account"
    }

    return render(request, 'post_error.html', context=context)

class AccountListView(generic.ListView):
    model = Account
    paginate_by = 25

class AccountDetailView(generic.DetailView):
    model = Account

class AccountByUserListView(LoginRequiredMixin, generic.ListView):
    """ Generic class-based view listing a users bank account(s). """
    model = Account
    template_name ='catalog/account_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Account.objects.filter(bank_user=self.request.user).order_by('balance')

class CardListView(generic.ListView):
    model = Card
    paginate_by = 25

class CardDetailView(generic.DetailView):
    model = Card

class CardByUserListView(LoginRequiredMixin, generic.ListView):
    """ Generic class-based view listing a users card(s). """
    model = Card
    template_name ='catalog/card_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Card.objects.filter(bank_user=self.request.user).order_by('account')

class TransactionListView(generic.ListView):
    model = Transaction
    paginate_by = 25

class TransactionDetailView(generic.DetailView):
    model = Transaction

class TransactionByUserListView(LoginRequiredMixin, generic.ListView):
    """ Generic class-based view listing a users card(s). """
    model = Transaction
    template_name ='catalog/transaction_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Transaction.objects.filter(bank_user=self.request.user).order_by('transaction_date')
