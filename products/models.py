from django.db import models

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    bar_code = models.CharField(max_length=13, unique=True)
    price = models.FloatField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='product_department')
    
    def __str__(self):
        return self.name
