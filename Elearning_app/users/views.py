from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.models import User

# Create your views here.

def index(request):
    return render(request, '/home/jaures/Documents/e-learning/Elearning_app/users/templates/utilisateurs/index.html', context={})


def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        image_profile = request.FILES.get('image_profile')
        bio = request.POST.get('bio')
        type_user = request.POST.get('type_user')
        if User.objects.filter(password=password, username=username).exists():
            return render(request, '/home/jaures/Documents/e-learning/Elearning_app/users/templates/utilisateurs/register.html',
                          context={'error': 'User already exists'})
        else:
            user = User.objects.create(username=username,
                                       first_name=first_name,
                                       last_name=last_name,
                                       password=password,
                                       image_profile=image_profile,
                                       bio=bio,
                                       type_user=type_user)
            user.save()
            return redirect('login')
    return render(request, '/home/jaures/Documents/e-learning/Elearning_app/users/templates/utilisateurs/register.html', context={})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render('/home/jaures/Documents/e-learning/Elearning_app/users/templates/utilisateurs/index.html')
        else:
            return render(request, '/home/jaures/Documents/e-learning/Elearning_app/users/templates/utilisateurs/login.html',
                          context={'error': 'User not found'})
    return render(request, '/home/jaures/Documents/e-learning/Elearning_app/users/templates/utilisateurs/login.html', context={})


def logout_user(request):
    logout(request)
    return redirect('login')