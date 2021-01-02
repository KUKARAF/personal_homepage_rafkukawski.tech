from django.db import models
from datetime import datetime 
class Painting(models.Model):
    painting_name = models.CharField(max_length=50)
    painting_author = models.CharField(max_length=30)
    painting_date = models.DateField()
    painting_id = models.AutoField(primary_key=True)
    painting_price = models.CharField(max_length=10)
    painting_desc = models.CharField(max_length=300)
    upload = models.FileField(upload_to='uploads/')

