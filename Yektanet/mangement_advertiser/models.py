import datetime
from django.db import models
from django.utils import timezone

class Advertiser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def incClicks(self):
        self.clicks += 1
        self.save()

    def incViews(self):
        self.views += 1
        self.save()

    @staticmethod
    def getTotalClicks():
        count = 0
        for i in Advertiser.objects.all():
            count += i.clicks
        return count

    def __str__(self):
        return self.name

class Ad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def incClicks(self):
        advertiser = Advertiser.objects.get(id=self.id)
        advertiser.incClicks()
        self.clicks += 1
        self.save()


    def incViews(self):
        advertiser = Advertiser.objects.get(id=self.id)
        advertiser.incViews()
        self.views += 1
        self.save()


    def __str__(self):
        return self.title