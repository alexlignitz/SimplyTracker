from django.contrib import admin
from django.urls import path, include
from tracker.views import IndexView, EmployeeAddView, ContractAddView, LocationAddView, PositionAddView, \
    AllEmployeesView, MainPageView, EmployeeDetailView, EmployeeDeleteView

urlpatterns = [
    #     GENERAL

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', IndexView.as_view(), name="index"),
    path('main/', MainPageView.as_view(), name="main"),

    #     EMPLOYEE MANAGEMENT

    path('employee_add/', EmployeeAddView.as_view(), name="employee_add"),
    path('employee_delete/<int:id>/', EmployeeDeleteView.as_view(), name="employee_delete"),
    path('contract_add/<int:id>/', ContractAddView.as_view(), name="contract_add"),
    path('employee_details/<int:id>/', EmployeeDetailView.as_view(), name="employee_details"),

    #     COMPANY MANAGEMENT
    path('location_add/', LocationAddView.as_view(), name="location_add"),
    path('position_add/', PositionAddView.as_view(), name="position_add"),

    #   REPORTS
    path('employee_list', AllEmployeesView.as_view(), name="employee_list"),

]



