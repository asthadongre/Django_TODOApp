from django.db import models

# Create your models here.
class Todo(models.Model):
    task=models.CharField(max_length=100, null=False, blank=False)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)