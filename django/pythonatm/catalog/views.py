from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from catalog.models import Account, Card, ATMachine, ATMachineRefill, Transaction
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.forms import CustomUserCreationForm, AccountCreationForm, PhoneChangeForm, CardCreationForm
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
            account = form.save()
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
    return render(request, "account_creation.html", context=context)

def CardView(request):
    if request.method == "POST":
        #account = Card(bank_user=request.user)
        #form = CardCreationForm(request.POST, instance=account)
        form = CardCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            Card = form.save()
            Card.bank_user = request.user
            Card.save()
            return redirect("my-cards")
        else:
            for msg in form.errors:
                print(form.errors[msg])

    form = CardCreationForm
    context = {
         'form' : form,
    }
    return render(request, "card_creation.html", context=context)

def TransactionView(request):
    form = PhoneChangeForm(request.POST)
    if form.is_valid():
        transaction = form.save(commit=False)
        transaction.bank_user = request.user
        transaction.save()
    context = {
         'form' : form,
    }
    return render(request, "phone_change.html", context=context)



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
        return Account.objects.filter(bank_user=self.request.user).order_by('account_number')

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
        return Card.objects.filter(bank_user=self.request.user).order_by('card_number')

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
        return Transaction.objects.filter(bank_user=self.request.user).order_by('transaction_id')
