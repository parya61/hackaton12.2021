from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='home'),
    path('', views.new,name='text'),
    path('file', views.new,name='file'),

]
