from django.urls import path

from . import views 

# /api/customers/
urlpatterns = [
    path('register/', views.customer_list_create_view, name='customer-list'),
    path('<int:pk>/update/', views.customer_update_view, name='customer-edit'),
    path('<int:pk>/delete/', views.customer_destroy_view),
    path('<int:pk>/', views.customer_detail_view, name='customer-detail')
]