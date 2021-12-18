from django.db import models


class Building(models.Model):
    project = models.CharField(max_length=30, null=False, blank=False)
    project_phase = models.CharField(max_length=30, null=True, blank=True)
    building_name = models.CharField(max_length=50, null=False, blank=False)
    building_type = models.CharField(max_length=50, null=False, blank=False)
    total_apartments = models.IntegerField(null=False, blank=True)

    def __str__(self):
        return self.building_name


class Apartment(models.Model):
    building_name = models.ForeignKey(Building, on_delete=models.CASCADE)
    apartment_no = models.IntegerField(null=False, blank=False)
    number_of_bedrooms = models.IntegerField(null=False, blank=False)
    floor_no = models.CharField(max_length=10, null=False, blank=False)
    notes = models.TextField(null=True, blank=True)
    profiles = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.building_name.building_name

