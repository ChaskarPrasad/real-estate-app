from django.db import models
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name  = models.CharField(max_length=100,null=True,blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    description = models.TextField(null=True,blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self) -> str:
        return self.name