from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views import View

from tracker.forms import AddEmployeeForm
from tracker.models import Employee


class IndexView(View):
    def get(self, request):
        return render(request, '__base__.html')


<<<<<<< HEAD
class MainPageView(View):
    def get(self, request):
        return render(request, 'main_page.html')
=======
class MainPageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'main_page.html')


class EmployeeListView(LoginRequiredMixin, View):
    pass


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
>>>>>>> origin/master
