from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Review(models.Model):
    usuario = models.CharField(max_length=255,default='No user',blank=True,null=False)
    
    book = models.ForeignKey(
        'books.Book',
        on_delete = models.CASCADE
    )
    review_text = models.TextField(default='No review yet')
    stars = models.IntegerField(default=1, validators=[MaxValueValidator(10),MinValueValidator(1)])
    
    def __str__(self) -> str:
        return f"{self.review_text}"