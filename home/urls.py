from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/info', views.info, name='api-info'),
    path('api/create_link_token', views.create_link_token, name='api-create-link-token'),
    path('exchange_public_token', views.exchange_public_token, name='api-exchange-public-token'),
    path('api/set_access_token', views.get_access_token, name='api-set_access_token'),
    path('api/auth', views.get_auth, name='api-auth'),
    path('api/transactions', views.get_transactions, name='api-transactions'),
    path('api/balance', views.get_balance, name='api-balance'),
    path('api/accounts', views.get_accounts, name='api-accounts'),
]
