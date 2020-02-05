from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default='False')

    def __str__(self):
        return self.username

class Msge(models.Model):
    body = models.CharField(max_length=280)
    msge_id = models.IntegerField(null=True)
    timestamp = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)
    last_st_change_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["msge_id"]
    
