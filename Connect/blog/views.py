from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import profile
from blog.models import blog
from blog.forms import blogform
from django.utils import timezone
import pytz
# Create your views here.
@login_required
def profileview(request):
    allprofile = profile.objects.all()
    finduser = request.user.username
    print(finduser)
    gotprofile = allprofile[0]
    profilecount = profile.objects.count()
    for i in range(profilecount):
        if allprofile[i].user == finduser:
            gotprofile = allprofile[i]
            break

    allblogs = blog.objects.all()
    blogcount = blog.objects.count()

    userblog = []
    for i in range(blogcount):
        if(allblogs[i].author == finduser):
            userblog.append(allblogs[i])


    mydict ={'profile' : gotprofile,'blogs' : userblog}

    return render(request,'blog/userprofile.html',mydict)
@login_required
def anyuserprofile(request):
    finduser = request.id
    allprofiles =  profile.objects.all()
    profilecount = profile.objects.count()
    for i in range(profilecount):
        if allprofile[i] == finduser:
            profile = allprofiles[i]
            break
    return render(request,'blog/anyuserprofile.html',{'profile' : profile})


@login_required
def putblog(request):
    form = blogform()
    if request.method == 'POST':
        recived = blogform(request.POST)
        if recived.is_valid():
            blogd = recived.cleaned_data['blogdata']
            timezone.activate(pytz.timezone("Asia/Kolkata"))
            blogobject = blog(author = request.user.username,blogdata =blogd,time=timezone.now())
            blogobject.save()
            return homepage(request)
        else:
            notify = 'please enter correct data'
            return render(request,'blog/putblog.html',{'notify':notify , 'blogform' : form})

    return render(request,'blog/putblog.html',{'blogform':form})


@login_required
def homepage(request):
    allblogs = blog.objects.all()

    mydict = {'allblogs' : allblogs}
    return render(request,'homepage.html',mydict)
