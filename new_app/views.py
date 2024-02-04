from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
from .models import Task, User_model
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password, check_password

@login_required(login_url="admin_login/")
def admin_home(request):
    return render(request,'admin.html')

def render_admin_login(request):
    return render(request,'admin_login.html')
    
def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_admin = authenticate(request, username=username, password=password)
            if user_admin:
                login(request, user_admin)
                return redirect('admin_home')
            else:
                return render(request, 'admin_login.html', {'form': form,'message': "Please try again!"})
    else:
        form = LoginForm()
    return render(request, 'admin_login.html', {'form': form,'message': ""})
            # username = request.POST['username']
            # password = request.POST['password']
            # user_db_objects = User_model.objects.filter(is_admin=1,user=username).values()
            # if user_db_objects.check_password(password):
            #     request.session["username"] = user_db_objects.user
            #     global logged_in
            #     logged_in = True
            #     return render(request,'admin.html')
            # return render(request,'login.html',{"message":"Wrong Credentials, Please try again"})

def render_admin_signup(request):
    return render(request,'admin_signup.html')

def admin_signup(request):
    render_admin_signup(request)
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('admin_login')
    else:
        form = UserCreationForm()
    return render(request, 'admin_signup.html', {'form': form})

    """username = request.POST['username']
    password = request.POST['password']"""
    """if username != "" and password != "":
        user_db = User_model.objects.create(user=username,password=make_password(password),is_admin=True)
        return redirect('admin_login')
    else:
        return redirect('admin_signup')"""

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

def push_data(request):
    app_name = request.POST['app_name']
    app_url = request.POST['app_url']
    category = request.POST['category']
    points = request.POST['points']
    image_file = request.FILES['image']
    print(image_file)
    tasks=Task.objects.create(app_name=app_name,app_url=app_url,category=category,points=points,img=image_file)
    return redirect('admin_home')

user_username = ""

def user_login(request):
    if request.method == 'POST': 
        form = LoginForm(request.POST)
        if form.is_valid():
            global user_username
            user_username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_user = authenticate(request, username=user_username, password=password)
            if user_user:
                login(request, user_user) 
                print("login succesful")
                return redirect('user_home')
            else:
                return render(request, 'user_login.html', {'form': form,'message': "Please try again!"})
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {'form': form,'message': ""})

def render_user_signup(request):
    return render(request,'user_signup.html')

def user_signup(request):
    render_user_signup(request)
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationForm()
    return render(request, 'user_signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url="user_login/")
def render_data(request):
    """elements = [{
        'app_name': 'Facebook',
        'app_url': '/facebook',
        'category': 'Social Media',
        'points': 50
    },{
        'app_name': 'LinkedIn',
        'app_url': '/linkedin',
        'category': 'Educational',
        'points': 50
    }]"""
    db_objects = Task.objects.all()
    #store = [db_objects.app_name,db_objects.app_url,"educational",50]
    print(db_objects[0])
    print(user_username)
    return render(request, 'user.html', {'elements': db_objects,'user':user_username})
"""
@login_required(login_url="/user/login_user/")
def user_home(request):
    redirect('user')"""