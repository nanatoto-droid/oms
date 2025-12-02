from django.db.models import Count
from .models import Order, OrderStatus

def order_stats():
    total = Order.objects.count()
    by_status = Order.objects.values('status').annotate(count=Count('id'))
    return {'total': total, 'by_status': list(by_status)}
