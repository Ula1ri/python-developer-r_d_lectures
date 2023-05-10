from rest_framework import serializers
from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('id', 'date', 'book_id_id', 'user_id_id')
