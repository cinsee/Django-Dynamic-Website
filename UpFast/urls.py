"""UpFast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_forms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index),
    path("register",views.register),
    path("checkRegister",views.checkRegister),
    path('login',views.login),
    path('checkLogin',views.checkLogin),
    path('logout',views.logout),
    path('createForm',views.createForm),
    path('user',views.userForm),
    path('userUpdate',views.userUpdate),
    path('addInput',views.addInput),
    path('saveForm',views.saveForm)
    # path("dashboard",views.dashboard),
    # path("draft",views.draft)
]
