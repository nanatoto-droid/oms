from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from .models import LoginLog

@receiver(user_logged_in)
def on_login(sender, request, user, **kwargs):
    LoginLog.objects.create(user=user, action='login')

@receiver(user_logged_out)
def on_logout(sender, request, user, **kwargs):
    if user:
        LoginLog.objects.create(user=user, action='logout')



        