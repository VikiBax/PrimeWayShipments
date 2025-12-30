from django.db import models
from .load import Load


class LoadCharge(models.Model):
    class ChargeType(models.TextChoices): 
        BASE = 'base', 'Base Rate', 
        LUMPER = 'lumper', 'Lumper',
        DETENTION = 'detention', 'Detention',
        LAYOVER = 'layover', 'Layover',
        TONU = 'tonu', 'TONU',
        OTHER = 'other', 'Other',
        REFUND = 'refund', 'Refund'

    class Direction(models.TextChoices): 
        EARNING = 'earning', 'Earning'
        DEDUCTION = 'deduction', 'Deduction'
        REFUND = 'refund', 'Refund'

    load = models.ForeignKey(Load, on_delete=models.PROTECT, related_name='charges')

    charge_type = models.CharField(max_length=20, choices=ChargeType.choices)
    description = models.CharField(max_length=255, blank=True, null=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    direction = models.CharField(max_length=10, choices=Direction.choices)
    taxable = models.BooleanField(default=True, help_text="Refunds and Reimbursements are usually not taxable.")

    created_at = models.DateTimeField(auto_now_add=True)