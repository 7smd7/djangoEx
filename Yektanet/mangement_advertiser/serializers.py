from rest_framework import serializers
from .models import Advertiser, Ad, Click, View, AbstractClickViews

class  AdvertiserSerializers(serializers.ModelSerializer):
    class  Meta:
        model = Advertiser
        fields = ['id','name']

class  AdSerializers(serializers.ModelSerializer):
    advertiser =  AdvertiserSerializers()
    class  Meta:
        model = Ad
        fields = ['id','advertiser','title','img_url','link','approve']

class  AbstractCVSerializers(serializers.ModelSerializer):
    ad = AdSerializers()
    class  Meta:
        model = AbstractClickViews
        fields = ['id','ad','time','ip']
        
class  ClickSerializers(serializers.ModelSerializer):
    class  Meta:
        model = Click
        fields = ['id','ad','time','ip']

class  ViewSerializers(serializers.ModelSerializer):
    ad = AdSerializers()
    class  Meta:
        model = View
        fields = ['id','ad','time','ip']
