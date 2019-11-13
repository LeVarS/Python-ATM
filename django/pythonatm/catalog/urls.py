from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.AccountListView.as_view(), name='accounts'),
    path('account/<int:pk>', views.AccountDetailView.as_view(), name='account-detail'),
]

urlpatterns += [
    path('myaccounts/', views.AccountByUserListView.as_view(), name='my-accounts'),
]

urlpatterns += [
    path('register/', views.register, name='register'),
]

urlpatterns += [
    path('cards/', views.CardListView.as_view(), name='cards'),
    path('card/<int:pk>', views.CardDetailView.as_view(), name='card-detail'),
    path('mycards/', views.CardByUserListView.as_view(), name='my-cards'),
]

urlpatterns += [
    path('transactions/', views.TransactionListView.as_view(), name='transaction'),
    path('transaction/<int:pk>', views.TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactionhistory/', views.TransactionByUserListView.as_view(), name='transaction-history'),
]

urlpatterns += [
    path('withdraw/', views.WithdrawTransactionView, name='withdraw'),
]

urlpatterns += [
    path('deposit/', views.DepositTransactionView, name='deposit'),
]

urlpatterns += [
    path('catalog/transfer', views.CashTransferView, name='transfer'),
]

urlpatterns += [
    path('createaccount/', views.AccountView, name='account-creation'),
]

urlpatterns += [
    path('createcard/', views.CardView, name='card-creation'),
]

urlpatterns += [
    path('editaccount/<int:pk>', views.EditAccountView, name='edit-account'),
]

urlpatterns += [
    path('editcard/<int:pk>', views.EditCardView, name='edit-card'),
]

urlpatterns += [
    path('fundserror/', views.InsufficientFundsView, name='insufficient-funds'),
]

urlpatterns += [
    path('accounterror/', views.AccountErrorView, name='nonexistent-account'),
]

urlpatterns += [
    path('atmfundserror/', views.AtmFundsErrorView, name='insufficient-atm-funds'),
]

urlpatterns += [
    path('atmcaperror/', views.AtmCapacityErrorView, name='insufficient-atm-capacity'),
]


# urlpatterns += [
#     path('register_account/', views.RegisterAccount, name='register_account'),
# ]
