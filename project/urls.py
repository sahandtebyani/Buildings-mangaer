from django.urls import path
from . import views

urlpatterns = [
    path('buildings', views.buildings_list, name='buildings'),
    path('buildings/<id>', views.apartments, name='building-apartments'),
    path('building-form', views.buildings_form, name='building-form'),
    path('apartment-form', views.apartments_form, name='apartment-form'),
]
