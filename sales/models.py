from django.db import models
from django.contrib.auth.models import User
from fruits.models import Fruit  


class Sale(models.Model):
    DISCOUNT_CHOICES = [
        (0.00, '0%'),
        (0.05, '5%'),
        (0.10, '10%'),
        (0.15, '15%'),
        (0.20, '20%'),
        (0.25, '25%'),
    ]
    
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    discount = models.DecimalField(max_digits=4, decimal_places=2, choices=DISCOUNT_CHOICES, default=0.00)
    total_value = models.DecimalField(max_digits=8, decimal_places=2)
    sale_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale of {self.fruit.name} by {self.seller.username}"