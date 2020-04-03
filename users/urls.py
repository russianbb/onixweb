from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    #Inlcude default auth urls
    path('', include('django.contrib.auth.urls')),
]