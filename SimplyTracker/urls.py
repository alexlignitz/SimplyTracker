from django.contrib import admin
from django.urls import path, include

from tracker.views import IndexView, MainPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', IndexView.as_view(), name="index"),
    path('main', MainPageView.as_view(), name="main"),
]
