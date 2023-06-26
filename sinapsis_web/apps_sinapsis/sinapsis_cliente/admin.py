from django.contrib import admin
from .models import SinapsisUser

# Register your models here.


@admin.register(SinapsisUser)
class SinapsisUserAdmin(admin.ModelAdmin):
    pass