from django.urls import path,include
from blog import views

urlpatterns =[
    path('homepage/profile',views.profileview,name= 'profileview'),
    path('homepage/putblog',views.putblog,name = 'blogsubmition')
]
