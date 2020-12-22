from django.db import models
from datetime import datetime 
class todo_item(models.Model):
    todo_name = models.CharField(max_length=30)
    todo_auth = models.CharField(max_length=30)
    due_date = models.DateField(auto_now_add=True)
    importance = models.IntegerField(default=1, blank=True)
    todo_id = models.AutoField(primary_key=True)
    required_time = models.IntegerField(default=1) # int meant to be used as relative multiplier for tasts used in pomodoro mode
    status = models.CharField(max_length=30, choices=[('new','new'),('o','ongoing'),('d','done'),('nd','not_doing'), ('h','hidden')], default='new')
