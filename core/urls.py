"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from grievance.views import (
    grievance,
    make_complaint,
    )
from account.views import (
    loginOptionPage,
    userLogin,
    adminLogin,
    dashboard,
    admin_dashboard,
    logoutView

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',loginOptionPage,name='loginOption'),
    path('logout',logoutView,name='logout'),
    path('login/user',userLogin,name='user_login'),
    path('login/admin',adminLogin,name='admin_login'),
    path('grievance',grievance),
    path('',dashboard,name='dashboard'),
    path('',admin_dashboard,name='admin_dashboard'),
    path('grievance/create',make_complaint,name='make_complaints'),
    
]
