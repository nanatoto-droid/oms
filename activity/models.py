from django.db import models
from django.conf import settings

class LoginLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=20)  # 'login' or 'logout'
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} {self.action} at {self.timestamp}'
    