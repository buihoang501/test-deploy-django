from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class UserProfileInfo(models.Model):
    #One to One relationship
    #Each user have each profile info
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #admintional
    portfolio_site = models.URLField(blank=True)

    profile_picture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
