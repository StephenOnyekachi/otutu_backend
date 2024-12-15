
import random
from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from .models import *

# Create your views here.

@login_required(login_url='login')
def users(request):
    profile = User.objects.filter(is_superuser=False)
    users = Profile.objects.all() #filter(user=profile)
    context = {
        'users':users
    }
    return render(request, 'users.html', context)

def deleteuser(request, pk):
    user = User.objects.get(username=pk)
    user.delete()
    messages.success(request, f"'{user.username}' was successfully deleted")
    return redirect('users')

@login_required(login_url='login')
def newuser(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        status = request.POST.get('status')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken, try again')
                return redirect("newuser")
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email have been used, try another email')
                return redirect("newuser")
            else:
                if status == "staff":
                    profile = User.objects.create_user(
                        username=username,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password,
                        is_staff = True
                    )
                    Profile.objects.create(
                        user=profile,
                        status=status,
                        phone=phone,
                    )
                    messages.success(request, f'you successfully created new user account "{username}"')
                    return redirect("users")
                else:
                    if status == "staff":
                        profile = User.objects.create_user(
                            username=username,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password,
                        )
                        Profile.objects.create(
                            user=profile,
                            status=status,
                            phone=phone,
                        )
                        messages.success(request, f'you successfully created new user account "{username}"')
                        return redirect("users")
        else:
            messages.info(request, "passwords doesn't match, try again")
            return redirect('newuser')
    return render(request, 'newuser.html')

@login_required(login_url='login')
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        "profile":profile,
    }
    return render(request, 'profile.html', context)

def Login(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'welcome back {username}')
            return redirect('profile')
        messages.info(request, 'username or password incorrect')
        return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken, try again')
                return redirect("signup")
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email have been used, try another email')
                return redirect("signup")
            else:
                profile = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
                Profile.objects.create(
                    user=profile,
                    status="customer",
                    phone=phone,
                )
                messages.success(request, f'you successfully created new user account "{username}"')
                return redirect("login")
        else:
            messages.info(request, "passwords doesn't match, try again")
            return redirect('signup')
    return render(request, 'signin.html')

def Logout(request):
    logout(request)
    return redirect('login')


