from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, '__base__.html')


class MainPageView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'main_page.html')