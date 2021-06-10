from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput

from tracker.models import Employee, Contract, Location, Position


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

    # def clean(self):
    #     data = super().clean()
    #     if position.level == 1 and 18000 < data['annual_salary'] <= 20000:
    #         return data
    #     elif self.position.level == 2 and 20000 < data['annual_salary'] <= 24000:
    #         return data
    #     elif self.position.level == 3 and 24000 < data['annual_salary'] <= 30000:
    #         return data
    #     elif self.position.level == 4 and 30000 < data['annual_salary'] <= 45000:
    #         return data
    #     elif self.position.level == 5 and 45000 < data['annual_salary'] <= 55000:
    #         return data
    #     elif self.position.level == 6 and 55000 < data['annual_salary'] <= 70000:
    #         return data
    #     elif self.position.level == 7 and data['annual_salary'] > 70000:
    #         return data
    #     else:
    #         raise ValidationError('Salary not in level range!')


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


class AddPositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'
