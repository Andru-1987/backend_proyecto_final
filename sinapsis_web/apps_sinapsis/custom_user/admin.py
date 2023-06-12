from django.contrib.admin import ModelAdmin
from django.contrib import admin

from apps_sinapsis.custom_user.models import CustomUser

@admin.register(CustomUser)
class ClienteAdmin(ModelAdmin):
    pass