from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from tracker.models import Employee, Contract, Location


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['login', 'email', 'is_active']


class DateInput(forms.DateInput):
    input_type = 'date'


class AddContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
        widgets = {
            'start_date': DateInput,
            'end_date': DateInput
        }


class AddLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

    def clean(self):
        data = super().clean()
        building_id = data['building_id']

        if Location.objects.filter(building_id=building_id).exists():
            raise ValidationError('Location already exists')
        else:
            return data
