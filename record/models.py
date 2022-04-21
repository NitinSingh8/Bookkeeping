from django.db import models

# Create your models here.
from datetime import  datetime

class OurRecord(models.Model):
    time = models.DateTimeField(blank=True,default=datetime.now())
    shop = models.TextField(blank=False)
    item = models.TextField(blank=False)
    price = models.FloatField(blank=False)

