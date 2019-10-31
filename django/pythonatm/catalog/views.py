from django.shortcuts import render
from catalog.models import Account, Card, ATMachine, ATMachineRefill, Transaction
from django.views import generic

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


class AccountListView(generic.ListView):
    model = Account
    paginate_by = 25

class AccountDetailView(generic.DetailView):
    model = Account
