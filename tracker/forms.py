from django import forms
from django.forms import DateInput

from tracker.models import Employee, Contract


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
