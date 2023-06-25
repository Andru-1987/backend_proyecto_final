from django.db import models

from apps_sinapsis.utils.Money import MONEY

from apps_sinapsis.utils.validate_functions import validate_ISBN
from django.utils.translation import gettext_lazy as _


class GENERO(models.Model):
    genero = models.CharField(max_length=154,unique=True,blank=False,null=False)

    def __str__(self) -> str:
        return f"{self.genero}"
    
    
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=245, default='Tienda-Online')
    
    def __str__(self) -> str:
        return f"{self.name}"

class Book(models.Model):

    nombre =  models.CharField(max_length=100)
    isbn =  models.CharField( 
        max_length=17,
        validators=[validate_ISBN],
        default="978-3-16-148410-0"
    
    )
    release_date = models.DateField(_("Date"), auto_now_add=True)
    genero  = models.ManyToManyField(GENERO)
    author = models.CharField(max_length=100)
    paginas = models.IntegerField(default=100, null=False , blank=True) 
    currency = models.CharField(
        max_length = 2,
        choices = MONEY.choices,
        default = MONEY.PESOS
    )
    precio = models.DecimalField(null=False,
                                  blank=False,
                                  default=1000.00,
                                  max_digits=12,
                                  decimal_places=2)

    sinapsis = models.TextField(default="Sin sinapsis aun cargadas")
    cantidad = models.IntegerField(default=10, null=False , blank=True) 
    store = models.ManyToManyField(Store)

    def __str__(self) -> str:
        return f"Titulo:\n{self.nombre} <|> ISBN:\t{self.isbn}"

    