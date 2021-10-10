from django.urls import include, path
from django.views.generic.base import RedirectView
from rest_framework import routers
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()
router.register(r'ad', views.AdViewSet)
router.register(r'advertiser', views.AdvertiserViewSet)
router.register(r'clickAndView', views.ClickAndViewViewSet)
router.register(r'click', views.ClickViewSet)
router.register(r'view', views.ViewViewSet)

app_name = 'mangement_advertiser'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('newad/', views.AdFormView.as_view() , name='newad'),
    path('query1/', views.Query1List.as_view() , name='query1'),
    path('query2/', views.Query2List.as_view() , name='query2'),
    path('query3/', views.Query3List.as_view() , name='query3'),
    path('click/<int:ad_id>/', views.ClickRedirectView.as_view(), name='click'),
    path('api/', include((router.urls))),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
