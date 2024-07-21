from django.views import View
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

class LoginView(View):
    def get(self, request: HttpRequest):
        return render(request, 'auth/login.html')
    
    def post(self, request: HttpRequest):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login_page') # TODO change for home or last_page
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login_page')