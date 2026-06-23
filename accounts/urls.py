from django.urls import path
from . import views

urlpatterns = [

path('login/register/',
     views.register,
     name='register'),

path("administrative/admin_register",
      views.admin_register,
        name="admin_register"),

path('login/',
     views.user_login,
     name='login'),

path('logout/',
     views.user_logout,
     name='logout'),

path('',views.home,
     name='home'),

path('administrative/',views.administrative_login,
     name='administrative_login'),


]