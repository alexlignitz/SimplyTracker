from django.shortcuts import render

from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, '__base__.html')


class MainPageView(View):
    def get(self, request):
        return render(request, 'main_page.html')
