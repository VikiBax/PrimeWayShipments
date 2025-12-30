from django.db import models

class BrokerCompany(models.Model):
    name = models.CharField(max_length=120, unique=True)
    mc_number = models.CharField(max_length=20, unique=True)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Broker Company'
        verbose_name_plural = 'Broker Companies'

    def __str__(self) -> str:
        return self.name
    

class BrokerAlias(models.Model): 
    broker_company = models.ForeignKey(BrokerCompany, on_delete=models.PROTECT, related_name='aliases')
    alias_name = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['alias_name']
        verbose_name = 'Broker Alias'
        verbose_name_plural = 'Broker Aliases'
        unique_together = ('broker_company', 'alias_name')

    def __str__(self) -> str:
        return f"{self.alias_name} ({self.broker_company.name})"