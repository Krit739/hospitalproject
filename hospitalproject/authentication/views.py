from django.shortcuts import render
from django.views import view

# Create your views here.
class loginView():
    def get(self, request):
        return render(request, 'authentication/login.html')