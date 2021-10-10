from django.contrib import admin

from .models import Advertiser
from .models import Ad, AdAdmin
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
admin.site.register(Advertiser)
admin.site.register(Ad, AdAdmin)