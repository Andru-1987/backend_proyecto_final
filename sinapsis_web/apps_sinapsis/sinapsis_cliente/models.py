from django.db import models
from django.contrib.auth.models import AbstractUser

class SinapsisUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True) 
    username = models.CharField( max_length =  150 , unique= False , blank=True , null =True )
    
    is_sinapsis_owner = models.BooleanField(default=False , unique=False , null=True , blank=True)
    is_sinapsis_manager = models.BooleanField(default=False,unique=False,null=True , blank=True)
    is_sinapsis_user = models.BooleanField(default=True,unique=False,null=True , blank=True )
    
    
    REQUIRED_FIELDS = [] 