"""Property_sale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showMain,name="main"),

    path('login/',views.loginCheck,name="login"),
    path('home/',views.home,name="home"),
    path('newplot/',views.newPlot,name="newplot"),
    path('saveplot/',views.savePlot,name="saveplot"),
    path('getplot/',views.getPlot,name="getplot"),
    path('viewplot/',views.viewPlot,name="viewplot"),
    path('viewplotdetail/',views.viewPlotDetail,name="viewplotdetail"),
    path('editplot/',views.editPlot,name="editplot"),
    path('update/',views.updatePlot,name="update"),
    path('update_plot/',views.plotUpdate,name="update_plot"),
    path('newflat/',views.newFlat,name="newflat"),
    path('saveflat/',views.saveFlat,name="saveflat"),
    path('getflat/',views.getFlat,name="getflat"),
    path('viewflat/',views.viewFlat,name="viewflat"),
    path('newemp/',views.newEmp,name="newemp"),
    path('saveemp/',views.saveEmp,name="saveemp"),
    path('viewemp/',views.viewEmp,name="viewemp"),
    path('editemp/',views.editEmp,name="editemp"),
    path('updateemployee/',views.updateEmp,name="updateemployee"),
    path('deleteemp/',views.deleteEmp,name="deleteemp"),
    path('about/',views.about,name="about"),



]
