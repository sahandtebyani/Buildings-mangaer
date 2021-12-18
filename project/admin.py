from django.contrib import admin
from .models import Apartment, Building


class BuildingAdmin(admin.ModelAdmin):
    list_display = ['project', '__str__', 'building_type']


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'apartment_no', 'floor_no']


admin.site.register(Building, BuildingAdmin)
admin.site.register(Apartment, ApartmentAdmin)

