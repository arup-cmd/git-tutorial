from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
# Create your views here.
def category(request,foo):
    foo = foo.replace('-','')
    try:
       category = Category.objects.get(name=foo)
       products = product.objects.fliter(category=category)
       return render(request,'category.html',{'products':products,'category':category})
    except: 
        messages.success(request,("that category Doesn't Except"))
        return redirect('home')   


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'Product':product})

def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'Products':products})

def about(request):
    return render(request,'about.html',{})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,("you have been logged In"))
            return redirect('home')
        else:
             messages.success(request,("There was an error,please try again"))
             return redirect('login')
    else:   
        return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.succes(request,("you have been logout"))
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm

def register_user(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user
            user = form.save()

            # Authenticate and login the user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You have registered successfully!")
                return redirect('home')
        else:
            # Display form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

    return render(request, 'register.html', {'form': form})

