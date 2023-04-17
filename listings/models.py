from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here.


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    zip = models.CharField(max_length=7,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    bedrooms = models.IntegerField(null=True,blank=True)
    bathrooms = models.IntegerField(null=True,blank=True)
    garage = models.BooleanField(default=True)
    sqft = models.IntegerField(null=True,blank=True)
    lot_size = models.DecimalField(max_digits=5,decimal_places=1,null=True,blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/",blank=True)

    def __str__(self):
        return self.title
    








