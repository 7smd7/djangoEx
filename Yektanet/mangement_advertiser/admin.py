from django.contrib import admin

from .models import Advertiser
from .models import Ad, AdAdmin

admin.site.register(Advertiser)
admin.site.register(Ad, AdAdmin)