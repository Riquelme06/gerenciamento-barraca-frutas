from django.db import models

# Create your models here.

class Fruit(models.Model):

    category_choices = [
        ('EXT', 'Extra'),
        ('PRI', 'Primeira'),
        ('SEG', 'Segunda'),
        ('TER', 'Terceira'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    category = models.CharField(max_length=3, choices = category_choices, blank=True, null=True)
    fresh_fruit =  models.BooleanField(default=True)
    quant = models.IntegerField(default=0)
    value =  models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


