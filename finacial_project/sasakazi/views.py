from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Accounts, Cards 
from .serializers import CustomerSerializer, AccountsSerializer, CardsSerializer
from .forms import AccountForm

# Create your views here.

def home(request):
    submitted = False
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')

    else:
        form = AccountForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'home.html', {'form': form, 'submitted': submitted})


class CustomerListCreateAPIView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None):
        if id:
            customer = Customer.objects.get(id=id)
            serializer = CustomerSerializer(customer)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
  


class AccountListCreateAPIView(APIView):
    def post(self, request):
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            account = Accounts.objects.get(id=id)
            serializer = AccountsSerializer(account)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        accounts = Accounts.objects.all()
        serializer = AccountsSerializer(accounts, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class CardListCreateAPIView(APIView):
    def post(self, request):
        serializer = CardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self, request, id=None):
        if id:
            card = Cards.objects.get(id=id)
            serializer = CardsSerializer(card)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        cards = Cards.objects.all()
        serializer = CardsSerializer(cards, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)



            