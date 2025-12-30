from django.db import models
from core.mixins import AddressMixin

# Create your models here.
class Driver(AddressMixin, models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        INACTIVE = 'inactive', 'Inactive'

    class PayType(models.TextChoices):
        Percentage = 'percentage', 'Percentage'
        Flat = 'flat', 'Flat Rate'
        cpm = 'cpm', 'Cents Per Mile'

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

    middle_name = models.CharField(max_length=80, blank=True, null=True)

    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    ssn_last4 = models.CharField(max_length=4, blank=True, null=True)
    ssn_full = models.CharField(max_length=11, blank=True, null=True)

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    notes = models.TextField(blank=True, null=True)

    pay_type = models.CharField(max_length=20, choices=PayType.choices, default=PayType.Percentage)
    default_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    default_flat_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    default_cpm = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    default_refunds_taxable = models.BooleanField(default=False)

    class Meta: 
        ordering = ['last_name', 'first_name']
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    @property 
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return self.full_name
    
    
