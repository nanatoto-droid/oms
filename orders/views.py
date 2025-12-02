from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order, OrderItem, OrderStatus
from products.models import Product
from .forms import AddToOrderForm

def is_customer(user): return user.groups.filter(name='customers').exists()
def is_admin(user): return user.is_staff or user.groups.filter(name='admins').exists()

@login_required
@user_passes_test(is_customer)
def my_orders(request):
    orders = Order.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})

@login_required
@user_passes_test(is_customer)
def add_to_order(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    if product.stock == 0:
        messages.error(request, 'Product is out of stock.')
        return redirect('products:list')

    # Create or reuse a pending order
    order, _ = Order.objects.get_or_create(customer=request.user, status=OrderStatus.PENDING)
    item, created = OrderItem.objects.get_or_create(
        order=order, product=product,
        defaults={'quantity': 1, 'price_snapshot': product.price}
    )
    if not created:
        item.quantity += 1
    item.price_snapshot = product.price
    item.save()

    product.stock -= 1  # reserve stock
    product.save()
    messages.success(request, 'Added to order.')
    return redirect('orders:my_orders')

@login_required
@user_passes_test(is_customer)
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    if order.status == OrderStatus.PENDING:
        # restore stock
        for item in order.items.all():
            p = item.product
            p.stock += item.quantity
            p.save()
        order.status = OrderStatus.CANCELLED
        order.save()
        messages.success(request, 'Order cancelled.')
    else:
        messages.error(request, 'Only pending orders can be cancelled.')
    return redirect('orders:my_orders')

@login_required
@user_passes_test(is_customer)
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    if order.status in [OrderStatus.CANCELLED, OrderStatus.PENDING]:
        # restore stock if pending
        if order.status == OrderStatus.PENDING:
            for item in order.items.all():
                p = item.product
                p.stock += item.quantity
                p.save()
        order.delete()
        messages.success(request, 'Order deleted.')
    else:
        messages.error(request, 'Delivered orders cannot be deleted.')
    return redirect('orders:my_orders')
