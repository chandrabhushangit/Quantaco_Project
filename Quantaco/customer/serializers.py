from rest_framework import serializers
from datetime import date
from .models import Customer
import re

class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = [
            
            'first_name', 
            'last_name', 
            'date_of_birth',
            'phone_number',
        ]

    def validate_first_name(self, value):
        """
        Check that the first name contains only alphabetic characters and is not empty.
        """
        if not value.isalpha():
            raise serializers.ValidationError("First name must contain only alphabetic characters.")
        return value

    def validate_last_name(self, value):
        """
        Check that the last name contains only alphabetic characters and is not empty.
        """
        print(value)
        if not value.isalpha():
            raise serializers.ValidationError("Last name must contain only alphabetic characters.")
        return value

    def validate_date_of_birth(self, value):
        """
        Check that the date of birth is a valid date .
        """
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 0 or age > 150:
            raise serializers.ValidationError("invalid date")
        return value
    def validate_phone_number(self, value):
        
        phone_pattern = re.compile(r'^(?:\+?\d{1,3})?[-. (]*(\d{1,4})[-. )]*(\d{1,4})[-. ]*(\d{1,9})$')
        if not phone_pattern.match(value):
            raise serializers.ValidationError("Invalid phone number format")
        return value
    
    def validate(self, data):
        """
        Check for duplicate customer data.
        """
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        date_of_birth = data.get('date_of_birth')
        phone_number = data.get('phone_number')
        
        if Customer.objects.filter(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, phone_number=phone_number).exists():
            raise serializers.ValidationError("A customer with these details already exists.")
        
        return data
   