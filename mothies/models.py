from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Mothie(models.Model):
    ask = models.CharField(max_length=500)
    reply = models.CharField(max_length=500, blank=True)
    is_replied = models.BooleanField(default=False)
    asked_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ask
