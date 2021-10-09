from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'mangement_advertiser'
urlpatterns = [
    path('', views.index, name='index'),
    path('newad/', views.newad, name='newad'),
    path('addad/', views.addad, name='addad'),
    path('click/<int:ad_id>/', views.click, name='click'),
]