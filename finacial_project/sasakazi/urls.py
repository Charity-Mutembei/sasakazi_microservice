from django.urls import path
from .views import (
    CustomerListCreateAPIView,
    # CustomerRetrieveUpdateDestroyAPIView,
    # AccountListCreateAPIView,
    # AccountRetrieveUpdateDestroyAPIView,
    # CardListCreateAPIView,
    # CardRetrieveUpdateDestroyAPIView,
)

urlpatterns=[
    # path('', views.index, name='index'),
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    # path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-retrieve-update-destroy'),
    # path('accounts/', AccountListCreateAPIView.as_view(), name='account-list-create'),
    # path('accounts/<int:pk>/', AccountRetrieveUpdateDestroyAPIView.as_view(), name='account-retrieve-update-destroy'),
    # path('cards/', CardListCreateAPIView.as_view(), name='card-list-create'),
    # path('cards/<int:pk>/', CardRetrieveUpdateDestroyAPIView.as_view(), name='card-retrieve-update-destroy'),
    
]