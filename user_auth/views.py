from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# LOGIN


def user_login(request):
    return render(request, 'user_auth/login.html', {})
