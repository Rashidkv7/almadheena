from django.urls import path
from . import views
urlpatterns =[
    path ('',views.login,name='login'),
    path ('signup',views.home,name='signup'),
    path ('signin',views.login,name='signin'),
    path ('home',views.home1,name='home_page'),
    
]