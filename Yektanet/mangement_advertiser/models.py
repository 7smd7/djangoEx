import datetime
from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db.models import AutoField
from django.contrib import admin
from django import forms
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


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
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class AdAdmin(admin.ModelAdmin):
    list_display = ('title','advertiser','approve')
    list_filter = ('approve','title','advertiser')
    list_editable = ['approve']
    search_fields = ['title']

class AbstractClickViews(models.Model):
    id = AutoField(primary_key=True)
    ad = models.ForeignKey(Ad,on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=16)

class Click(AbstractClickViews):
    pass

class View(AbstractClickViews):
    pass

