from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Employee(AbstractUser): 
    ROLE_ADMIN = 'admin' 
    ROLE_DISPATCHER = 'dispatcher'
    ROLE_ACCOUNTING = 'accounting'
    ROLE_OFFICE = 'office'
    ROLE_MAINTENANCE = 'maintenance'

    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_DISPATCHER, 'Dispatcher'),
        (ROLE_ACCOUNTING, 'Accounting'),
        (ROLE_OFFICE, 'Office'),
        (ROLE_MAINTENANCE, 'Maintenance'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
    )

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username 
    
