from django.db import models

# Create your models here.
class user(models.Model): 
    user_id = models.CharField(max_length=23) 
    name = models.CharField(max_length=100) 
    age = models.IntegerField
     
    def __str__(self):
        return self.name