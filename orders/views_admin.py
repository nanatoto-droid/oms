from django.contrib.auth.decorators import user_passes_test, login_required
from .services import order_stats
from django.db.models import Count
from .models import Order
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm




def is_admin(user):
     return user.is_staff or user.groups.filter(name='admins').exists()

def is_admin(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    stats = order_stats()
    return render(request, 'admin/dashboard.html', {'stats': stats})


@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'orders/admin_dashboard.html', {'orders': orders})

@login_required
@user_passes_test(is_admin)
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders:admin_dashboard')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:admin_dashboard')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})