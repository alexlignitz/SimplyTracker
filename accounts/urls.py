from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import RegistrationView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    # NEW USER REGISTRATION (ADMIN ONLY)
    path('registration/', RegistrationView.as_view(), name="registration"),

    # PASSWORD RESET URLS
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset/password_reset_done.html"),
         name="password_reset_complete"),

    # PASSWORD CHANGE URLS
    path('change_password/',
         auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"),
         name="password_change"),
    path('change_password_done/',
         auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_complete.html"),
         name="password_change_done"),
]