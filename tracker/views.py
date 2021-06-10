from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views import View

from tracker.forms import AddEmployeeForm, AddContractForm, AddLocationForm
from tracker.models import Employee


class IndexView(View):
    def get(self, request):
        return render(request, '__base__.html')


class MainPageView(LoginRequiredMixin, View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'main_page.html', {'employees': employees})


class EmployeeDetailView(LoginRequiredMixin, View):
    pass


class EmployeeAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddEmployeeForm
        return render(request, 'form.html', {'form': form, 'header': 'Add employee'})

    def post(self, request):
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.login = employee.create_login()
            employee.email = employee.create_email()
            employee.save()
            return render(request, 'employee_details.html',
                          {'msg': 'Employee added to database', 'href': '/main/', 'employee': employee})
        return render(request, 'form.html', {'form': form, 'header': 'Add employee'})


class EmployeeEditView(LoginRequiredMixin, View):
    pass


class EmployeeDeleteView(LoginRequiredMixin, View):
    pass


class ContractAddView(View):
    def get(self, request, id):
        form = AddContractForm(initial={'employee': id})
        return render(request, 'form.html', {'form': form, 'header': 'Add contract'})

    def post(self, request, id):
        employee = Employee.objects.get(pk=id)
        form = AddContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.employee = employee
            contract.save()
            return render(request, 'add_confirmation.html', {'object': 'contract'})


class LocationAddView(View):
    def get(self, request):
        form = AddLocationForm
        return render(request, 'form.html', {'form': form, 'header': 'Add location'})

    def post(self, request):
        form = AddLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_confirmation.html', {'object': 'location'})
        return render(request, 'form.html', {'form': form, 'header': 'Add location'})
