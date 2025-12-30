from django.db import models
from companies.models import Company

# Create your models here.
class Truck(models.Model): 
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        IN_SHOP = 'in_shop', 'In Shop'
        INACTIVE = 'inactive', 'Inactive'
        Sold = 'sold', 'Sold'

    unit_number = models.CharField(max_length=30, unique=True)
    vin = models.CharField(max_length=17, unique=True)

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    registration_expiration = models.DateField(blank=True, null=True)
    inspection_expiration = models.DateField(blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['unit_number']
        verbose_name = 'Truck'
        verbose_name_plural = 'Trucks'

    def __str__(self) -> str:
        return f"Truck {self.unit_number}" 
    


class Trailer(models.Model): 
    class Status(models.TextChoices): 
        ACTIVE = 'active', 'Active'
        IN_SHOP = 'in_shop', 'In Shop'
        INACTIVE = 'inactive', 'Inactive'
        Sold = 'sold', 'Sold'

    class TrailerType(models.TextChoices):
        DRY_VAN = 'dry_van', 'Dry Van'
        REEFER = 'reefer', 'Reefer'
        FLATBED = 'flatbed', 'Flatbed'
        Step_DECK = 'step_deck', 'Step Deck'
        Other = 'other', 'Other'

    unit_number = models.CharField(max_length=30, unique=True)
    vin = models.CharField(max_length=17, unique=True)

    trailer_type = models.CharField(max_length=20, choices=TrailerType.choices, default=TrailerType.DRY_VAN)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)

    registration_expiration = models.DateField(blank=True, null=True)
    inspection_expiration = models.DateField(blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['unit_number']
        verbose_name = 'Trailer'
        verbose_name_plural = 'Trailers'
    
    def __str__(self) -> str:
        return f"Trailer {self.unit_number}"
    
    