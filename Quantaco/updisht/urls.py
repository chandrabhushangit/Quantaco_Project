from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.models import Token
from .views import Dashboard,Submit


urlpatterns = [
    # path('', Login.as_view(),name="Login"),
    path('api/dashboard/', Dashboard.as_view(),name="dashboard"),
    path('api/submit/', Submit.as_view(),name="submit"),
    # path('dashboard1/', views.dashboard1,name="dashboard1"),
    # path('admin/', admin.site.urls),
    # path('api/dashboard', ),  # Define a view function to handle the root URL
   
]