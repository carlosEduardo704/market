from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from localflavor.br.models import BRStateField, BRPostalCodeField

MAX_ADDRESSES_PER_USER = 3

class Adress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_adress')
    adress_name = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    number = models.CharField(max_length=6)
    zip_code = BRPostalCodeField()
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    uf = BRStateField(verbose_name='UF')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def clean(self):
        if not self.pk:
            if Adress.objects.filter(user=self.user).count() >= MAX_ADDRESSES_PER_USER:
                raise ValidationError(f"Um usuário não pode ter mais de {MAX_ADDRESSES_PER_USER} endereços cadastrados!")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.adress_name}, {self.street}, {self.number}, {self.city}"
