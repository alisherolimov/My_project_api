from django.urls import path
from . import views

urlpatterns = [
    path('get-all-cars/', views.get_all_car),
    path('get-all-repairs_and_services/', views.get_all_repairs_and_services),
    path('get-car-by-region/<int:pk>/', views.get_car_by_region),
    path('get-car-by-district/<int:pk>/', views.get_car_by_district),
    path('get-repairs_and_services-by-region/<int:pk>/', views.get_repairs_and_services_by_region),
    path('search-car-by-name/', views.search_car_by_name),
    path('search-repairs-and-services-by-name/', views.search_repairs_and_services_by_name),
    path('filter-car-by-light/', views.filter_car_by_light),
    path('filter-car-by-not-light/', views.filter_car_by_not_light),
    path('filter-car-by-rent/', views.filter_car_by_rent),
    path('filter-car-by-not-rent/', views.filter_car_by_not_rent),
    path('filter-car-by-bargaining/', views.filter_car_by_bargaining),
    path('filter-car-by-not-bargaining/', views.filter_car_by_not_bargaining),
    path('filter-car-by-automat/', views.filter_car_by_automat),
    path('filter-car-by-mechanic/', views.filter_car_by_mechanic),
    path('add-favorites-car/<int:pk>/', views.add_favorites_car),
    path('add-favourites-repairs-and-services/<int:pk>/', views.add_favourites_repairs_and_services),
    path('get-all-favourites/', views.get_all_favourites),
    path('update-cars-view/<int:pk>/', views.update_cars_view),
    path('create_comment/<int:pk>/', views.create_comment),
]