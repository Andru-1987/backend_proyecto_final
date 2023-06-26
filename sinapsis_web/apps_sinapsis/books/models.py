from django.db import models
from django.db.models.query import QuerySet

from apps_sinapsis.utils.Money import MONEY

from apps_sinapsis.utils.validate_functions import validate_ISBN
from django.utils.translation import gettext_lazy as _


class GENERO(models.Model):
    genero = models.CharField(max_length=154,unique=True,blank=False,null=False)

    def __str__(self) -> str:
        return f"{self.genero}"
    

class StoreManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().exclude(status=False)


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=245, default='Tienda-Online')
    status = models.BooleanField(default=True)
    provincia = models.CharField(max_length=100,default="Buenos Aires")
    location_src = models.TextField(
        default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3285.830022710853!2d-58.68286492323899!3d-34.55785885507963!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcbc45fa07e48f%3A0x2ede182f3817f97e!2sLa%20Plata%20889%2C%20B1661HYL%20Bella%20Vista%2C%20Provincia%20de%20Buenos%20Aires!5e0!3m2!1sen!2sar!4v1687761473818!5m2!1sen!2sar"
    )
    horarios = models.CharField(max_length=100, default= "Lunes a Viernes de 9am a 18pm")

    
    objets_all = models.Manager()
    objects = StoreManager()
    
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
    short_sinapsis = models.TextField(default="Sinapsis corta")
    cantidad = models.IntegerField(default=10, null=False , blank=True) 
    store = models.ManyToManyField(Store)
    
    image_url = models.ImageField(
        null=True, blank=True , upload_to= "images/" ,default="images/bg_book.jpg"
    )

    def __str__(self) -> str:
        return f"Titulo:\n{self.nombre} <|> ISBN:\t{self.isbn}"

    