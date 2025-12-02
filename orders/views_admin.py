from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from .services import order_stats

def is_admin(user): return user.is_staff or user.groups.filter(name='admins').exists()

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    stats = order_stats()
    return render(request, 'admin/dashboard.html', {'stats': stats})
