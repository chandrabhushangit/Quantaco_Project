from rest_framework import serializers

from .models import Customer


class ProductSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Customer
        fields = [
            
            'first_name', 
            'last_name', 
            'date_of_birth',
            'phone_number',
        ]
    
   