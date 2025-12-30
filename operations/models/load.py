from django.db import models
from companies.models import Company
from drivers.models import Driver
from assets.models import Trailer, Truck
from accounts.models import Employee
from .broker import BrokerAlias 
from django.core.exceptions import ValidationError


class Load(models.Model):
    class Status(models.TextChoices):
        DISPATCHED = 'dispatched', 'Dispatched',
        DELIVERED = 'delivered', 'Delivered', 
        SETTLED = 'settled', 'Settled',
    load_number = models.CharField(max_length=30, unique=False)

    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='loads')
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT, related_name='loads')
    dispatcher = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='loads')

    truck = models.ForeignKey(Truck, on_delete=models.PROTECT, related_name='loads')
    trailer = models.ForeignKey(Trailer, on_delete=models.PROTECT, related_name='loads', blank=True, null=True)

    broker_alias = models.ForeignKey(BrokerAlias, on_delete=models.PROTECT, related_name='loads')

    status = models.CharField(max_length=15, choices=Status.choices, default=Status.DISPATCHED)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    pickup_scheduled = models.DateTimeField(blank=True, null=True)
    pickup_actual = models.DateTimeField(blank=True, null=True)

    delivery_scheduled = models.DateTimeField(blank=True, null=True)
    delivery_actual = models.DateTimeField(blank=True, null=True)


    empty_location = models.CharField(max_length=255, blank=True, null=True)
    pickup_location = models.CharField(max_length=255, blank=True, null=True)
    delivery_location = models.CharField(max_length=255, blank=True, null=True)

    contact_info = models.CharField(max_length=255, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)

    base_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    miles = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    locked_at = models.DateTimeField(blank=True, null=True)

    class Meta: 
        ordering = ['-created_at']
        verbose_name = 'Load'
        verbose_name_plural = 'Loads'

    def __str__(self) -> str:
        shown = self.load_number or f"#{self.pk}" 
        return f"Load {shown}"
    
    @property
    def rate_per_mile(self): 
        if not self.miles or self.miles == 0:
            return None
        return self.base_rate / self.miles
    
    def clean(self): 
        # if settled, it must be locked 
        if self.status == self.Status.SETTLED and not self.locked_at: 
            raise ValidationError('Settled loads must be locked.')
        

    def save(self, *args, **kwargs):
        # prevent edits once locked 
        if self.pk: 
            old = Load.objects.get(pk=self.pk)
            if old.locked_at: 
                raise ValidationError('Cannot edit a locked load.')
        super().save(*args, **kwargs)
        

