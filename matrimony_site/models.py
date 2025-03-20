from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    bio = models.TextField(max_length=500)
    profession = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)
    # Add other relevant fields for matrimony profiles
    
    def __str__(self):
        return self.user.username
class ModelName(models.Model):
    class Meta:
        def __str__(self):
            return self.field_name