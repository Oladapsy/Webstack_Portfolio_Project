from django.shortcuts import render
from rest_framework import viewsets
from .models import Client, Invoice, Item
from .serializers import ClientSerializer, InvoiceSerializer, ItemSerializer

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
        queryset = Invoice.objects.all()
        serializer_class = InvoiceSerializer

class ItemViewSet(viewsets.ModelViewSet):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer
