from .models import Advertiser
from .models import Ad
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    context = {'advertisers': []}
    advertiser_list = Advertiser.objects.all()
    for i in range(0,len(advertiser_list)):
        temp= advertiser_list[i]
        ad_list = advertiser_list[i].ad_set.all()
        temp.ads = ad_list.values();
        context['advertisers'].append(temp)
        for j in range(0,len(ad_list)):
            ad_list[j].incViews()
        advertiser_list[i].save()
    return render(request, "ads.html", context)

def detail(request, advertiser_id):
    advertiser = get_object_or_404(Advertiser, pk=advertiser_id)
    return render(request, 'detail.html', {'advertiser': advertiser})

def click(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    ad.incClicks()

    return HttpResponseRedirect(ad.link)