from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Accounts, Cards 
from .serializers import CustomerSerializer, AccountsSerializer, CardsSerializer

# Create your views here.

class CustomerListCreateAPIView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

# class AccountListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Accounts.objects.all()
#     serializer_class = AccountsSerializer

# class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Accounts.objects.all()
#     serializer_class = AccountsSerializer

# class CardListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Cards.objects.all()
#     serializer_class = CardsSerializer

# class CardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cards.objects.all()
#     serializer_class = CardsSerializer