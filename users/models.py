from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=255, default='https://cdn-icons-png.flaticon.com/512/21/21294.png')

    def __str__(self):
        return f"{self.user.username} Profile "

