from .models import Advertiser, Ad, Click, View, AbstractClickViews
from .serializers import AdvertiserSerializers, AdSerializers, ClickSerializers, ViewSerializers, AbstractCVSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView
from django.db.models import Count
from django.db.models.functions import Trunc
from itertools import chain, groupby
from rest_framework import viewsets, generics
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class Index(TemplateView):
    
    template_name = "ads.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisers'] =  []
        advertiser_list = Advertiser.objects.all().order_by('name')
        for i in range(0,len(advertiser_list)):
            temp= advertiser_list[i]
            ad_list = advertiser_list[i].ad_set.filter(approve = True)
            temp.ads = ad_list.values();
            context['advertisers'].append(temp)
            for j in range(0,len(ad_list)):
                view = View(ad = ad_list[j], ip=kwargs['ip'])
                view.save()
        return context

class AdFormView(CreateView):
    template_name = 'newad.html'
    model = Ad
    fields = ['id', 'advertiser', 'title', 'img_url', 'link']
    success_url = '/mangement_advertiser/'

class ClickRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'ad_id'

    def get_redirect_url(self, *args, **kwargs):
        ad = get_object_or_404(Ad, pk=kwargs['ad_id'])
        self.url = ad.link
        click = Click(ad=ad,ip=kwargs['ip'])
        click.save()
        return super().get_redirect_url(*args, **kwargs)

class Query1List(TemplateView):
    template_name = 'q1.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = AbstractClickViews.objects.values('ad','time').annotate(key=Trunc('time', 'hour')).values('ad','key').annotate(count = Count('key')).order_by('key')
        for i in range(len(context['query'])):
            context['query'][i]['ad_title'] = Ad.objects.get(id=context['query'][i]['ad'])
        return context

class Query2List(TemplateView):
    template_name = 'q2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = []
        a = Click.objects.values('ad','time').annotate(key=Trunc('time', 'hour')).values('ad','key').annotate(countClick = Count('key')).order_by('key')
        b = View.objects.values('ad','time').annotate(key=Trunc('time', 'hour')).values('ad','key').annotate(countView = Count('key')).order_by('key')
        result_list = list( sorted(chain(a,b),key=lambda row: (row['key'],row['ad'])))
        for i in range(len(result_list)-1)[::-1]:
            if (result_list[i]['key']==result_list[i+1]['key'] and result_list[i]['ad']==result_list[i+1]['ad']):
                c = {**result_list[i],**result_list[i+1]}
                context['query'].append(c)
        for i in range(len(context['query'])):
            context['query'][i]['ad_title'] = Ad.objects.get(id=context['query'][i]['ad'])
            context['query'][i]['ratio'] = float("{:.3f}".format( context['query'][i]['countClick']/context['query'][i]['countView'] ))
        return context

class Query3List(TemplateView):
    template_name = 'q3.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = []
        a = Click.objects.values('ad','ip','time').annotate(countClick=Count('ad'))
        b = View.objects.values('ad','ip','time').annotate(countView=Count('ad'))
        result_list = list( sorted(chain(a,b),key=lambda row: (row['ip'],row['ad'],row['time'])))
        for i in range(len(result_list)-1):
            if (result_list[i]['ad']==result_list[i+1]['ad'] and 
                result_list[i]['ip']==result_list[i+1]['ip'] and
                'countView' in result_list[i].keys() and
                'countClick' in result_list[i+1].keys()):
                c = {'ad': result_list[i]['ad'], 'ip':result_list[i]['ip'],
                    # 'timeView':result_list[i]['time'],'timeClick':result_list[i+1]['time'],
                    'difference': result_list[i+1]['time']-result_list[i]['time']}
                context['query'].append(c)
        sum = context['query'][0]['difference']-context['query'][0]['difference']
        for i in range(len(context['query'])):
            context['query'][i]['ad_title'] = Ad.objects.get(id=context['query'][i]['ad'])
            sum += context['query'][i]['difference']
        context['avg']=sum/len(context['query'])
        return context

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializers

class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializers

class ClickAndViewViewSet(viewsets.ModelViewSet):
    queryset = AbstractClickViews.objects.all()
    serializer_class = AbstractCVSerializers

class ClickViewSet(viewsets.ModelViewSet):
    queryset = Click.objects.all()
    serializer_class = ClickSerializers

class ViewViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializers