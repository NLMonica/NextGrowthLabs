from django.db import models

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your models here.

class Task(models.Model):
    app_name = models.CharField(max_length=30)
    app_url = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    sub_category = models.CharField(max_length=30)
    points = models.IntegerField()
    img = models.ImageField(upload_to='images/', default=None,blank=True, null=True)
    def __unicode__(self):
        return "{0} {1} {2} {3} {4} {5}".format(self, self.app_name,self.app_url,self.category,self.sub_category,self.points,self.img)

class User_model(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    is_admin = models.BooleanField()

