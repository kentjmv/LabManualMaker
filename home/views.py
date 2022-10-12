# Imports
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .filters import LabFilter
from .forms import *

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return 0
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                
            else:
                messages.info(request,'Username OR Password is incorrect')

    return render(request, "main/authenticate.html")

def home(request):
    if request.method == 'POST':
        searched = request.POST['searched']

        return redirect('mainsite:search', pk=searched)
    else:
        return render(request, "main/home.html")

def about_us(request):
    return render(request, "main/aboutus.html")

def contact(request):
    return render(request, "main/contact.html")

def searchpage(request, pk):
    if request.method == 'POST':
        searched = request.POST['searched']

        return redirect('mainsite:search', pk=searched)
    else: 
        return render(request, "main/search.html", {
            'searched': pk,
        })

def createlab(request):
    
    form = NewLab()


    return render(request, 'main/createlab.html', {
        'form': form,
        })
