from django.db import models
from apps_sinapsis.custom_user.models import CustomUser

# Create your models here.
class Cliente(CustomUser):
    editor = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.email}"