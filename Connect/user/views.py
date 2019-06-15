from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from blog.models import blog,profile
from blog.views import profileview



# Create your views here.
def index(request):
    return render(request,'user/index.html')

@login_required
def homepage(request):
    allblogs = blog.objects.all()

    mydict = {'allblogs' : allblogs}
    return render(request,'homepage.html',mydict)

def log_in(request):
    return render(request,'user/login.html')

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        recived = UserCreationForm(request.POST)
        if recived.is_valid():
            recived.save()

            gotuser = recived.cleaned_data['username']
            gotpass = recived.cleaned_data['password1']

            userprofile=profile.objects.create(user = gotuser)
            userprofile.save()


            user = authenticate(username = gotuser,password = gotpass)
            login(request,user)
            return HttpResponseRedirect('/homepage')

    dict = {'form':form}
    return render(request,'user/signup.html',dict)


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login')
