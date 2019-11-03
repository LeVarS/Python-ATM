from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', views.AccountListView.as_view(), name='accounts'),
    path('cards/', views.CardListView.as_view(), name='cards'),
    path('account/<int:pk>', views.AccountDetailView.as_view(), name='account-detail'),
    path('card/<int:pk>', views.CardDetailView.as_view(), name='card-detail'),
]

urlpatterns += [
    path('myaccounts/', views.AccountByUserListView.as_view(), name='my-accounts'),
]

urlpatterns += [
    path('register/', views.register, name='register'),
]

urlpatterns += [
    path('mycards/', views.CardByUserListView.as_view(), name='my-cards'),
]

# urlpatterns += [
#     path('register_account/', views.RegisterAccount, name='register_account'),
# ]
