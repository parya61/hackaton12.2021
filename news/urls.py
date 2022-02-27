from django.urls import path
from . import views


urlpatterns = [
        path('', views.text,name='text'),
        path('file/', views.file,name='file'),
        path('baza/', views.baza,name='baza'),
        # path('fileload', views.fileload,name='fileload'),


]
