from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Moviedata(models.Model):
    def __str__(self): #This is used in order to view the 'movie name' in django admin and not as 'Moviedata object'
        return self.name
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=200,default='Action')
    image = models.ImageField(upload_to='Images/',default='Images/None/Noimg.jpg')