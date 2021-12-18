from django import forms
from .models import Building, Apartment


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'
        widgets = {
            'project': forms.TextInput(attrs={'class': 'form-control'}),
            'project_phase': forms.TextInput(attrs={'class': 'form-control'}),
            'building_name': forms.TextInput(attrs={'class': 'form-control'}),
            'building_type': forms.TextInput(attrs={'class': 'form-control'}),
            'total_apartments': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'
        widgets = {
            'building_name': forms.Select(attrs={'class': 'form-control'}),
            'apartment_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_of_bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'floor_no': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control','rows': "5"}),
            'profiles': forms.NumberInput(attrs={'class': 'form-control'}),
        }
