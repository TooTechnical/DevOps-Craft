from django.db import models
from users.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Days to deliver")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent = models.CharField(max_length=100)
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
