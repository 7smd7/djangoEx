from .models import Advertiser, Ad, Click, View
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView

class Index(TemplateView):
    
    template_name = "ads.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advertisers'] =  []
        advertiser_list = Advertiser.objects.all()
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