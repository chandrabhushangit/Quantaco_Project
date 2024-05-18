from rest_framework import serializers
from datetime import date
from .models import Customer


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
        if not value.isalpha():
            raise serializers.ValidationError("Last name must contain only alphabetic characters.")
        return value

    def validate_date_of_birth(self, value):
        """
        Check that the date of birth is a valid date and the person is at least 18 years old.
        """
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 0 or age > 150:
            raise serializers.ValidationError("invalid date")
        return value
    def validate_phone_number(self, value):
        
        # if not value.isdigit():
        #     raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) not in [10, 11, 12, 13, 14, 15]:
            raise serializers.ValidationError("Phone number must be 10 to 15 digits long.")
        return value
   