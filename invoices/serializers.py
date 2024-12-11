from rest_framework import serializers
from .models import UnifiedModel

class UnifiedModelSerializer(serializers.ModelSerializer):
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UnifiedModel
        fields = [
            'id', 'user', 'name', 'email', 'address', 'phone_number',
            'invoice_number', 'date_issued', 'due_date', 'description', 'status',
            'item_title', 'quantity', 'price', 'total_amount'
        ]
        read_only_fields = ['invoice_number', 'total_amount', 'user']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        if not validated_data.get('invoice_number'):
            validated_data['invoice_number'] = self.Meta.model().generate_invoice_number()
        return super().create(validated_data)
