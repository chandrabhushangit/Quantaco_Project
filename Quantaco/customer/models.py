from django.db import models
from django.utils import timezone
# Create your models here.
class Customer(models.Model):
    # pk
    
    first_name = models.CharField(max_length=120, default="")
    last_name = models.CharField(max_length=120)
    date_of_birth = models.DateField(default=timezone.now)
    phone_number = models.CharField(max_length=15, default="")
    def __str__(self):
        return f"{self.first_name} "
    # class Meta:
    #     # Specify the table name
    #     db_table = 'products_customer'