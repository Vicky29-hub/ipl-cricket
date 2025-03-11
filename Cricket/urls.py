"""Cricket URL Configuration

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
from cricketapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views.login),
    path('register/',views.register),
    path('clubregister/',views.clubregister),
    path('adminhome/',views.adminhome),
    path('clubhome/',views.clubhome),
    path('customerhome/',views.customerhome),
    path('club/',views.club),
    path('Approve/',views.approve),
    path('Deleteclub/',views.deleteclub),
    path('customers/',views.customers),
    path('Delete/',views.delete),
    path('fixture/',views.addfixtures),
    path('players/',views.addplayers),
    path('news/',views.addnews),
    path('viewfixtures/',views.viewfixtures),
    path('addresult/',views.addresult),
    path('feedback/',views.feedback),
    path('complaint/',views.complaint),
    path('viewnews/',views.viewnews),
    path('newsdetail/',views.viewnewsdetail),
    path('viewclub/',views.viewclub),
    path('viewfixtures_cust/',views.viewfixtures_cust),
    path('viewfeedback/',views.viewfeedback),
    path('viewcomplaint/',views.viewcomplaint),
    path('viewplayer/',views.viewplayers),
    path('viewclub_basedplayer/',views.viewclub_based_players),
    path('viewplayers_customer/',views.viewplayer_cus),
    path('toss_prediction/',views.toss_prediction),
    path('score_prediction/',views.score_prediction),
    path('score_prediction_cust/',views.score_prediction_cust),
    path('toss_prediction_cust/',views.toss_prediction_cust),
    


]
