from django.contrib import admin
from django.urls import path, include

<<<<<<< HEAD
from tracker.views import IndexView, MainPageView
=======
from tracker.views import IndexView, MainPageView, EmployeeAddView
>>>>>>> origin/master

urlpatterns = [
    #     GENERAL

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', IndexView.as_view(), name="index"),
<<<<<<< HEAD
    path('main', MainPageView.as_view(), name="main"),
=======
    path('main/', MainPageView.as_view(), name="main"),

    #     EMPLOYEE MANAGEMENT

    path('employee_add/', EmployeeAddView.as_view(), name="employee_add"),
>>>>>>> origin/master
]
