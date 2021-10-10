from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'mangement_advertiser'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('newad/', views.AdFormView.as_view() , name='newad'),
    path('query1/', views.Query1List.as_view() , name='query1'),
    path('query2/', views.Query2List.as_view() , name='query2'),
    path('query3/', views.Query3List.as_view() , name='query3'),
    path('click/<int:ad_id>/', views.ClickRedirectView.as_view(), name='click'),
]