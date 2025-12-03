from django.urls import path
from .views import my_orders, add_to_order, cancel_order, delete_order
from .views_admin import admin_dashboard
from . import views
from . import views_admin

urlpatterns = [
    path('my/', my_orders, name='my_orders'),
    path('add/<int:product_id>/', add_to_order, name='add'),
    path('cancel/<int:order_id>/', cancel_order, name='cancel'),
    path('delete/<int:order_id>/', delete_order, name='delete'),
    path('admin-dashboard/', views_admin.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/add/', views_admin.add_order, name='add_order'),
    path('admin-dashboard/update/<int:order_id>/', views_admin.update_order, name='update_order'),
]


