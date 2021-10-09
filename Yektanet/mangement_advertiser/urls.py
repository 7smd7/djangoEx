from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'mangement_advertiser'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('newad/', views.AdFormView.as_view() , name='newad'),
    path('click/<int:ad_id>/', views.ClickRedirectView.as_view(), name='click'),
]