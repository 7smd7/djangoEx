from django.contrib import admin

from .models import Advertiser
from .models import Ad

admin.site.register(Advertiser)
admin.site.register(Ad)