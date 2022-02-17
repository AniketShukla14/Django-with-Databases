from django.db import models

# Create your models here.
class member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    password = models.CharField(max_length=50)
  
    def __str__(self):
        return self.fname+ " "+self.lname 
        #To prevent name to be displayed as Objects this is used 