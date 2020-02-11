from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django import forms

# Create your models here.

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default='False')

    def __str__(self):
        return self.username

class Msge(models.Model):
    body = models.TextField(max_length=280)
    msge_id = models.IntegerField(null=True, blank=True)
    timestamp = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20)
    last_st_change_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ["msge_id"]
    
