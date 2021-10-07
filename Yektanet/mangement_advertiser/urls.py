from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'mangement_advertiser'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    # path('<int:ad_id>/', views.detail, name='detail'),
    # ex: /polls/5/vote/
    path('click/<int:ad_id>/', views.click, name='click'),
]