from django.urls import path
from .views import get_countries, send_country,update_country,delete_country,selecte_one

urlpatterns  = [
    path('countries/', get_countries, name= "get_country"),
    path('countries/new/', send_country, name= "new_country"),
    path('countries/update/<str:country>/', update_country, name= "update_country"),
    path('countries/delete/<str:country>/', delete_country, name= "delete_country"),
    path('countries/select_one/<str:country>/', selecte_one, name= "select_one_country"),

]