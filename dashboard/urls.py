from django.urls import path
from .views import create_car, update_car, delete_car, create_repairs_and_services, update_repairs_and_services, delete_repairs_and_services

urlpatterns =[
    path('create-car/', create_car),
    path('update-car/<int:pk>/', update_car),
    path('delete-car/<int:pk>/', delete_car),
    path('create-repairs-and-services/', create_repairs_and_services),
    path('update-repairs-and-services/<int:pk>/', update_repairs_and_services),
    path('delete-repairs-and-services/<int:pk>/', delete_repairs_and_services),
]