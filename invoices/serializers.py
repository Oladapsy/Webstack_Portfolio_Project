from rest_framework import serializers
from .models import Client, Invoice, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Invoice
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'