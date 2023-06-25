from django.db import models
from django.db.models.query import QuerySet


class UserSinapsisManager(models.Manager):
    
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().exclude(
            active = False
        )


class UserSinapsis(models.Model):
    class Meta:
        abstract = True
        
    nombre = models.CharField(max_length = 100,null=False , blank=False) 
    apellido = models.CharField(max_length = 100, null=False , blank=False)
    email = models.CharField(max_length = 200,unique=True, null=False,blank=False)
    deleted_date = models.DateTimeField(default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    