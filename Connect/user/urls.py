from django.urls import path,include
from user import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog import urls

urlpatterns =[
    path('',views.index,name = 'index'),
    path('signup/',views.sign_up,name = 'signup'),
    path('homepage/',views.homepage,name = 'home'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/',views.log_out,name = "logout"),
    path('',include(urls))
]
