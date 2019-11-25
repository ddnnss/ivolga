from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', views.robots, name='robots'),
    path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
    path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
    #path('services/', views.services, name='services'),
    path('service/<slug>/', views.service, name='service'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('callback/', views.callback, name='callback'),


]