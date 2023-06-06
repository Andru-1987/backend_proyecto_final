from django.db import models
from django.contrib.auth.models import AbstracUser
# Create your models here.

class CustomUser(AbstracUser):
    pic = models.CharField(max_length=100, null=True, blank=True)


    