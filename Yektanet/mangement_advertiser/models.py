import datetime
from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db.models import AutoField

class Advertiser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ad(models.Model):
    id = models.BigIntegerField(primary_key=True)
    advertiser = models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class AbstractClickViews(models.Model):
    id = AutoField(primary_key=True)
    ad = models.ForeignKey(Ad,on_delete=models.CASCADE)
    advertiser = models.ForeignKey(Advertiser,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=16)

class Click(AbstractClickViews):
    pass

class Views(AbstractClickViews):
    pass

