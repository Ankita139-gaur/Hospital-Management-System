# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import *
from .models import *
def register(request):

    if request.method == "POST":

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request,'register.html')

def admin_register(request):

    if request.method=="POST":
        name=request.POST['name']
        email = request.POST['email']
        registration_no=request.POST['regisrtation']
        password=request.POST['password']

        User.objects.create_user(
            name=name,
            email=email,
            registration_no=registration_no,
            password=password
        )

        return redirect(administrative_login)
    return render(request,'admin_register.html')

def user_login(request):

    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user:

            login(request,user)

            return redirect('dashboard')

    return render(request,'login.html')

def administrative_login(request):

    if request.method == "POST":

        regisrtation = request.POST['regisrtation']

        password = request.POST['password']

        administrative = authenticate(
            regisrtation=regisrtation,
            password=password
        )

        if administrative:

            login(request,administrative)

            return redirect('dashboard')

    return render(request,'administrative_login.html')

def user_logout(request):

    logout(request)

    return redirect('login')
def home(request):
    return render(request,'home.html')