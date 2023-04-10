from django.db import models
class studentmodel(models.Model):
    name=models.CharField(max_length=100)
    rollnbr=models.IntegerField()
    city=models.CharField(max_length=100) 

# Create your models here.
