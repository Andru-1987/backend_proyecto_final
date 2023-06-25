from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

class MONEY(TextChoices):
    DOLARES = 'US' , _('Dolares')
    PESOS = 'PS' , _('Pesos Argentinos')
    EUROS = 'EU' ,_('Euros')
        