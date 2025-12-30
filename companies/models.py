from django.db import models
from django.core.validators import RegexValidator

from core.mixins import AddressMixin

# Create your models here.
class Company(AddressMixin,models.Model):
    name = models.CharField(max_length=120, unique=True)
    active = models.BooleanField(default=True)

    ein = models.CharField( 
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{2}-\d{7}$',
                message='EIN must be in the format XX-XXXXXXX',
            ),
        ],
        help_text='Enter EIN in the format XX-XXXXXXX',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies' 

    def __str__(self) -> str: 
        return self.name
    

