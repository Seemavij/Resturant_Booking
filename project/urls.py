"""
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
    2. Add a URL to urlpatterns:  path('reservation/', include('reservation.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from resturant.views import IndexPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', IndexPage.as_view(), name='index'),
  #  path("", include('reservation.urls'), name='reservation-urls'),
  #  path('resturant/', include ('resturant.urls'), name='resturant-urls'),
  #  path('summernote/', include('django_summernote.urls')),
    path('table_reservation/', include('reservation.urls', namespace='table_reservation')),
    path('menu_list/', include('menu.urls', namespace='menu_list')),
    path('manage_reservation/', include('reservation.urls', namespace='manage_reservation'))
 

 ]
admin.site.site_header = 'Delhi Darbar AdminPanel'
       
 
     
 
  

    
    

