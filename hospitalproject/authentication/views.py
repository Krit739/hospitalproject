from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User

# Create your views here.
class loginView():
    def get(self, request):
        return render(request, 'authentication/login.html')

class registerView(View):

    def get(self, request):
        return render(request, 'authentication/register.html')
    def post(self, request):
        req_username=request.POST.get('username')
        req_email=request.POST.get('email')
        req_password=request.POST.get('password')
        user =User.objects.create_user(email=req_email, username=req_username)
        user.set_password(req_password)
        user.is_active= True
        user.is_staff=False
        user.is_superuser=False
        user.save()

        # context={

        #     "email": req_email,
        #     "password": req_password,
        #     "username": req_username,
        # }
        return render(request, 'authenticaton/register.html')