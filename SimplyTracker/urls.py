from django.contrib import admin
from django.urls import path, include
from tracker.views import IndexView, MainPageView, EmployeeAddView, ContractAddView, LocationAddView

urlpatterns = [
    #     GENERAL

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', IndexView.as_view(), name="index"),
    path('main/', MainPageView.as_view(), name="main"),

    #     EMPLOYEE MANAGEMENT

    path('employee_add/', EmployeeAddView.as_view(), name="employee_add"),
    path('contract_add/<int:id>/', ContractAddView.as_view(), name="contract_add"),

    #     COMPANY MANAGEMENT
    path('location_add/', LocationAddView.as_view(), name="location_add"),
]
