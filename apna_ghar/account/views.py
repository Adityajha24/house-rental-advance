from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
from django.views import View

class Createaccount(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        print(request.POST)
        user = User.objects.filter(username=request.POST.get('username'))
        if user:
            messages.add_message(request, messages.ERROR, "Username allready exist")
            return render(request, 'signup.html')
        if request.POST.get('password') != request.POST.get('password1'):
            messages.add_message(request, messages.ERROR, "Password Does not match")
            return render(request, 'signup.html')
        passa = make_password(request.POST.get('password'))
        User.objects.create(username=request.POST.get('username'),
            password=passa)
        messages.add_message(request, messages.SUCCESS, "User has been created")
        return render(request, 'signup.html')

class Login(View):
    def get(self, request):
        return render(request, 'imdex.html')
    def post(self, request):
        return render(self, 'MINOR.html')

