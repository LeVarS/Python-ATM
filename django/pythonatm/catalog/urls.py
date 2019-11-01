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
