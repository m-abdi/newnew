from distutils.sysconfig import get_makefile_filename
from email.policy import default
from types import CoroutineType
from django.db import models

from uuid import uuid4
from datetime import datetime
# Create your models here.
class Data(models.Model):
    # id = models.CharField(primary_key=True , default= uuid4().hex , max_length= 400)
    name= models.CharField("name", max_length=100)
    title = models.CharField("title", max_length=100)
    about_me = models.CharField("about_me" ,  max_length=200)
    phone = models.CharField("phone", max_length=20)
    gmail = models.CharField("Gmail" , null= True , max_length=100 )
    city = models.CharField("city", max_length=20)
    knowledge = models.CharField("knowledge", max_length=200)
    skills = models.JSONField("skills", default=list)
    instagram = models.CharField("instagram" , max_length=20 )
    time = models.FloatField(default=datetime.now().timestamp())

    def __str__(self) -> str:
        return self.name
    