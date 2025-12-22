from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from localflavor.br.models import BRStateField, BRPostalCodeField

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_adress')
    adress_name = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=6)
    zip_code = BRPostalCodeField()
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    uf = BRStateField(verbose_name='UF')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.adress_name}, {self.street}, {self.number}, {self.zip_code}, {self.city}, {self.district}, {self.uf}"
