from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from orders.models import Order
from products.models import Product

class Command(BaseCommand):
    help = 'Seed default groups and permissions'

    def handle(self, *args, **options):
        customers, _ = Group.objects.get_or_create(name='customers')
        admins, _ = Group.objects.get_or_create(name='admins')

        # Customers can add/cancel/delete their own orders via views logic;
        # still give them read permissions for products.
        product_ct = ContentType.objects.get_for_model(Product)
        view_product = Permission.objects.get(codename='view_product', content_type=product_ct)
        customers.permissions.add(view_product)

        # Admins get all permissions
        for perm in Permission.objects.all():
            admins.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Groups seeded'))
