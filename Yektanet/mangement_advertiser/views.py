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

def newad(request):
    return render(request, 'newad.html', {})

def addad(request):
    req = dict(request.POST)
    for i in req.keys():
        req[i]=req[i][0]
    req['ad_id'] = int(req['ad_id'])
    req['advertiser_id'] = int(req['advertiser_id'])
    if(Ad.objects.get(id = req['ad_id'])):
        return HttpResponse("The id was used.")
    advertiser = get_object_or_404(Advertiser, pk=req['advertiser_id'])
    ad = Ad(id=req['ad_id'], advertiser = advertiser,title=req['title'],img_url=req['img_url'],link=req['link'])
    ad.save()
    return HttpResponseRedirect('/mangement_advertiser/')

def click(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)
    ad.incClicks()

    return HttpResponseRedirect(ad.link)