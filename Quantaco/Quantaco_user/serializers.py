# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # You can include additional fields here if necessary
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required = True)
    
    class Meta:
        model = User
        # Define the fields that should be serialized
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        """
        Check that the two password entries match.
        """
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        # Remove password_confirm from validated data
        validated_data.pop('password_confirm')
        
        # Create a new user instance
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        # Set the user's password
        user.set_password(validated_data['password'])
        user.save()
        return user
