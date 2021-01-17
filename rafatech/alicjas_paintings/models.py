from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime 
import base64





class Painting(models.Model):
    painting_name = models.CharField(max_length=50)
    painting_author = models.CharField(max_length=30)
    painting_date = models.DateField()
    painting_id = models.AutoField(primary_key=True)
    painting_price = models.DecimalField(max_digits=5, decimal_places=2)
    painting_desc = models.CharField(max_length=300)
    upload = models.FileField(upload_to='static/ap/uploads/')
    painting_dimensions = models.CharField(max_length=30)

class Imgs(models.Model ):
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    img_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='static/ap/uploads/')



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
