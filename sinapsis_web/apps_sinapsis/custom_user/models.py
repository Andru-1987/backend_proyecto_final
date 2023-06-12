from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin



class CustomUserManager(BaseUserManager):
    
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be an requested value, sorry 🙂')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=70,unique=True)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Retorna el nombre completo del usuario.
        """
        return self.name

    def get_short_name(self):
        """
        Retorna el nombre abreviado del usuario.
        """
        return self.name