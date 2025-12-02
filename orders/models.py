from django.db import models
from django.conf import settings
from products.models import Product

class OrderStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    DELIVERED = 'delivered', 'Delivered'
    CANCELLED = 'cancelled', 'Cancelled'
    OUT_OF_STOCK = 'out_of_stock', 'Out of Stock'

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): return f'Order #{self.id} by {self.customer.username}'

    def total_items(self):
        return sum(item.quantity for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price_snapshot = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self): return f'{self.product.name} x{self.quantity}'


    