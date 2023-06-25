from django.contrib import admin

from .models import Book
from .models import GENERO
from .models import Store

# Register your models here.

@admin.register(Book)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(GENERO)
class GeneroAdmin(admin.ModelAdmin):
    pass

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass