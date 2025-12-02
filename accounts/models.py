from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Extra fields for sign-up
    start_date = models.DateField(null=True, blank=True)  # "When are you starting?"
    # username, email, first_name, last_name, password exist already

def profile_upload_path(instance, filename):
    return f'profiles/user_{instance.user_id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to=profile_upload_path, blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'Profile({self.user.username})'