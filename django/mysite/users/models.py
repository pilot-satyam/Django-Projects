from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #importing the User details and using on delete cascade
    img = models.ImageField(default='profilepic.jpg',upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    def __str__(self): #string representation of the model
        return self.user.username  #whenever we are trying to access the object of that model we want to get the username
