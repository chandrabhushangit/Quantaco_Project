# myapp/models.py
from django.db import models
from datetime import datetime
import random
from django.contrib.auth.models import AbstractUser,User
class Updisht(models.Model):
    S_No = models.IntegerField(null=True)
    First_Name = models.CharField(max_length=255, null=True)
    Last_Name = models.CharField(max_length=255, null=True)
    Guardian_Type = models.CharField(max_length=255, null=True)
    Guardian_Name = models.CharField(max_length=255, null=True)
    Gender = models.CharField(max_length=10, null=True)
    Age = models.IntegerField(null=True)
    Contact_no = models.CharField(max_length=45, null=True)
    Email_ID = models.CharField(max_length=255, null=True)
    Education_Qualification = models.CharField(max_length=255, null=True)
    Occupation = models.CharField(max_length=255, null=True)
    Vill_Mohalla = models.CharField(max_length=255, null=True)
    Post = models.CharField(max_length=255, null=True)
    City = models.CharField(max_length=255, null=True)
    District = models.CharField(max_length=255, null=True)
    State = models.CharField(max_length=255, null=True)
    Pin = models.IntegerField(null=True)
    Date_of_Updesh = models.IntegerField(null=True)
    Place_of_Updesh = models.CharField(max_length=255, null=True)
    Name_Of_Motivator = models.CharField(max_length=255, null=True)
    Motivator_Contact_No = models.CharField(max_length=20, null=True)
    Motivator_Address = models.CharField(max_length=255, null=True)
    Updeshta_Name = models.CharField(max_length=255, null=True)
    Updeshta_Contact_No = models.CharField(max_length=20, null=True)
    Address = models.CharField(max_length=255, null=True)
    Date_Of_Calling = models.CharField(max_length=50, null=True)
    Caller_Introduction = models.CharField(max_length=255, null=True)
    Comfortable_Language = models.CharField(max_length=255, null=True)
    Sadhna = models.CharField(max_length=255, null=True)
    Photo = models.CharField(max_length=255, null=True)
    Aarti_Vandana = models.CharField(max_length=255, null=True)
    Remarks = models.TextField(null=True)
    Call_on_8586808820_For_More_Information = models.CharField(max_length=10, null=True)
    Comment = models.TextField(null=True)
    Caller_Name = models.CharField(max_length=255, null=True)
    Caller_No = models.CharField(max_length=20, null=True)
    Group_Leader_Name = models.CharField(max_length=255, null=True)
    Group_Leader_No = models.CharField(max_length=20, null=True)
    Status_of_call = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'updisht_submit'
        app_label = 'CallerApp'

class UpdishtSubmit(models.Model):
    S_No = models.IntegerField(null=True)
    First_Name = models.CharField(max_length=255, null=True)
    Last_Name = models.CharField(max_length=255, null=True)
    Guardian_Type = models.CharField(max_length=255, null=True)
    Guardian_Name = models.CharField(max_length=255, null=True)
    Gender = models.CharField(max_length=10, null=True)
    Age = models.IntegerField(null=True)
    Contact_no = models.CharField(max_length=45, null=True)
    Email_ID = models.CharField(max_length=255, null=True)
    Education_Qualification = models.CharField(max_length=255, null=True)
    Occupation = models.CharField(max_length=255, null=True)
    Vill_Mohalla = models.CharField(max_length=255, null=True)
    Post = models.CharField(max_length=255, null=True)
    City = models.CharField(max_length=255, null=True)
    District = models.CharField(max_length=255, null=True)
    State = models.CharField(max_length=255, null=True)
    Pin = models.IntegerField(null=True)
    Date_of_Updesh = models.IntegerField(null=True)
    Place_of_Updesh = models.CharField(max_length=255, null=True)
    Name_Of_Motivator = models.CharField(max_length=255, null=True)
    Motivator_Contact_No = models.CharField(max_length=20, null=True)
    Motivator_Address = models.CharField(max_length=255, null=True)
    Updeshta_Name = models.CharField(max_length=255, null=True)
    Updeshta_Contact_No = models.CharField(max_length=20, null=True)
    Address = models.CharField(max_length=255, null=True)
    Date_Of_Calling = models.CharField(max_length=50, null=True)
    Caller_Introduction = models.CharField(max_length=255, null=True)
    Comfortable_Language = models.CharField(max_length=255, null=True)
    Sadhna = models.CharField(max_length=255, null=True)
    Photo = models.CharField(max_length=255, null=True)
    Aarti_Vandana = models.CharField(max_length=255, null=True)
    Remarks = models.TextField(null=True)
    Call_on_8586808820_For_More_Information = models.CharField(max_length=10, null=True)
    Comment = models.TextField(null=True)
    Caller_Name = models.CharField(max_length=255, null=True)
    Caller_No = models.CharField(max_length=20, null=True)
    Group_Leader_Name = models.CharField(max_length=255, null=True)
    Group_Leader_No = models.CharField(max_length=20, null=True)
    Status_of_call = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'updisht_submit'
        app_label = 'CallerApp'

def create_new_ref_number():
    return str(random.randint(1000000000, 9999999999) - random.randint(1, 200) + int(datetime.now().strftime('%M%S')) - random.randint(1, 200))
class CustomUser(AbstractUser):
    '''Model for User'''
    GROUP_NM = models.CharField(max_length=100,
                                choices=[('SUPER', 'SUPER'), ('CALLER', 'CALLER')])
    GROUP_ID = models.CharField(max_length=100,
                                choices=[('0', 0), ('1', 1)])

    GROUP_LEAD = models.CharField(max_length=100)
    GROUP_LEAD_EMAIL_ID = models.CharField(max_length=100)
    USER_KEY = models.CharField(max_length=100,
                                unique=True,
                                editable=True,
                                default=create_new_ref_number())

    class Meta:
        # In admin
        verbose_name_plural = "  Users"
        app_label = 'CallerApp'
    def __str__(self):
        return self.username


class AccessUser(models.Model):
    '''Model For User Access'''
    ACTV_FLG = models.CharField(max_length=100,
                                choices=[('Y', 'Active'), ('N', 'Deactive')])
    
    
    User_ID = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, db_column='User_ID')
    ACCESS_KEY = models.CharField(max_length=10,
                                  blank=True,
                                  editable=True,
                                  unique=True,
                                  default=create_new_ref_number()
                                  )

    class Meta:
        verbose_name_plural = " Access"
        app_label = 'CallerApp'
    def __str__(self):
        return str(self.User_ID)