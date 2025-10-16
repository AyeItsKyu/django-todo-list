from django.db import models
from django.contrib.auth.models import User

class Task(models.Model): 
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256,blank=True,null=True)
    is_completed = models.BooleanField(default=False, blank=True)
    complete_dt = models.DateField(blank=True,null=True)