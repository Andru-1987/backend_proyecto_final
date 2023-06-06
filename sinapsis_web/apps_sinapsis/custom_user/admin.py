from django.contrib import admin
from apps_sinapsis.custom_user.models import CustomUser

@admin.register(CustomUser)
class ClienteAdmin(admin.ModelAdmin):
    pass