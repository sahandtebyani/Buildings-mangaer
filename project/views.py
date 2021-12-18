from django.shortcuts import render, get_object_or_404, redirect
from .models import Apartment, Building
from .forms import BuildingForm, ApartmentForm


def buildings_list(request):
    buildings = Building.objects.all()
    context = {'buildings': buildings}
    return render(request, 'buildings.html', context)


def apartments(request, id):
    building = get_object_or_404(Building, id=id)
    apartment_list = Apartment.objects.filter(building_name=building)
    context = {
        'building_name': building,
        'apartments': apartment_list
    }
    return render(request, 'apartments.html', context)


def buildings_form(request):
    if request.method == 'POST':
        building_form = BuildingForm(request.POST or None)
        if building_form.is_valid:
            building_form.save()
        return redirect('buildings')
    else:
        building_form = BuildingForm()
    context = {
        'building_form': building_form
    }
    return render(request, 'buildings_form.html', context)


def apartments_form(request):
    if request.method == 'POST':
        apartment_form = ApartmentForm(request.POST or None)
        if apartment_form.is_valid:
            apartment_form.save()
        return redirect('apartment-form')
    else:
        apartment_form = ApartmentForm()
    context = {'apartment_form': apartment_form}
    return render(request, 'apartments_form.html', context)
