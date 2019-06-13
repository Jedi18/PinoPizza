from django.db import models

# Create your models here.
class PizzaAndSubs(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    small = models.DecimalField(decimal_places=2, max_digits=8)
    large = models.DecimalField(decimal_places=2, max_digits=8)
    ispizza = models.BooleanField()

class Others(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    small = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    large = models.DecimalField(decimal_places=2, max_digits=8)
    isdinnerplatter = models.BooleanField()

class ToppingsAndExtra(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    isextra = models.BooleanField()
