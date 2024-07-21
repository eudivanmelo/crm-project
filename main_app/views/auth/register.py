from django.views import View
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group

class RegisterView(View):
    def get(self, request: HttpRequest):
        return render(request, 'auth/register.html')
    
    def post(self, request: HttpRequest):
        first_name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register_page')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register_page')
        
        user = User(username=username,
                          first_name=first_name,
                          email=email,
                          password=make_password(password)
                          )
        user.save()
        
        group = Group.objects.get(name='operator')

        if group is None:
            messages.error(request, 'An error occurred, please try again later!')
            print('Invalid group in register view!')
            return redirect('register_page')
        
        user.groups.add(group)
        return redirect('login_page')