from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    deviceNumber = models.IntegerField()
    def __unicode__(self):
        return self.username