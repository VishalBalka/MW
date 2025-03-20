from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone_number = models.CharField(max_length=15, blank=True)
    email_verified = models.BooleanField(default=False)
    account_type = models.CharField(
        max_length=20,
        choices=[
            ('SELF', 'Self'),
            ('PARENT', 'Parent/Guardian'),
            ('SIBLING', 'Sibling'),
            ('RELATIVE', 'Relative'),
            ('FRIEND', 'Friend'),
        ],
        default='SELF'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"