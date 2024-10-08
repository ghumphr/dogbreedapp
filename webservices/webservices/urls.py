"""
URL configuration for webservices project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from dogapi.views import rest_get_dog
#from dogapi.views import rest_get_breed
from rest_framework.urlpatterns import format_suffix_patterns
from dogapi import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # These URLs were used in the initial REST test and are deprecated
    #path('rest/dog/<int:dog_id>/', rest_get_dog, name='rest_get_dog'),
    #path('rest/breed/<int:breed_id>/', rest_get_breed, name='rest_get_breed'),

    path('api/dogs/', views.DogList.as_view()),
    path('api/dogs/<int:dog_id>/', views.DogDetail.as_view()),
    path('api/breeds/', views.BreedList.as_view()),
    path('api/breeds/<int:breed_id>/', views.BreedDetail.as_view()),
]
