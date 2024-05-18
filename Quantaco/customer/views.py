from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Customer
from .serializers import CustomerSerializer

class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
       
        serializer.save()
        

customer_list_create_view = CustomerListCreateAPIView.as_view()

class CustomerDetailAPIView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    

customer_detail_view = CustomerDetailAPIView.as_view()


class CustomerUpdateAPIView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        # if not instance.content:
        #     instance.content = instance.title
            ## 

customer_update_view = CustomerUpdateAPIView.as_view()


class CustomerDestroyAPIView(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

customer_destroy_view =CustomerDestroyAPIView.as_view()

