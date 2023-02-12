from django.urls import path
from .views import (
    CustomerListCreateAPIView,
    # AccountListCreateAPIView,
    # AccountRetrieveUpdateDestroyAPIView,
    # CardListCreateAPIView,
    # CardRetrieveUpdateDestroyAPIView,
)

urlpatterns=[
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customer/<int:id>', CustomerListCreateAPIView.as_view(), name='cutomer-id'),
    # path('accounts/', AccountListCreateAPIView.as_view(), name='account-list-create'),
    # path('accounts/<int:pk>/', AccountRetrieveUpdateDestroyAPIView.as_view(), name='account-retrieve-update-destroy'),
    # path('cards/', CardListCreateAPIView.as_view(), name='card-list-create'),
    # path('cards/<int:pk>/', CardRetrieveUpdateDestroyAPIView.as_view(), name='card-retrieve-update-destroy'),
    
]