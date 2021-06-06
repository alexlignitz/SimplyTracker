from django import forms

from tracker.models import Employee


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['login', 'email', 'is_active']
