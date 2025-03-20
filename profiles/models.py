from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    # User relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Basic Details
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('NM', 'Never Married'),
        ('DIV', 'Divorced'),
        ('WID', 'Widowed'),
        ('SEP', 'Separated'),
    ]
    
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=3, choices=MARITAL_STATUS_CHOICES)
    about_me = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    
    # Physical attributes
    height = models.IntegerField(help_text="Height in centimeters")
    body_type = models.CharField(max_length=50, blank=True)
    
    # Location
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    
    # Religion and community
    religion = models.CharField(max_length=100)
    mother_tongue = models.CharField(max_length=100)
    community = models.CharField(max_length=100, blank=True)
    
    # Education and career
    education = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    income = models.CharField(max_length=50, blank=True)
    
    # Family details
    family_type = models.CharField(max_length=50, blank=True)
    family_status = models.CharField(max_length=50, blank=True)
    family_values = models.CharField(max_length=50, blank=True)
    
    # Lifestyle
    diet = models.CharField(max_length=50, blank=True)
    smoking = models.CharField(max_length=50, blank=True)
    drinking = models.CharField(max_length=50, blank=True)
    
    # Partner Preferences
    partner_age_min = models.IntegerField(default=18)
    partner_age_max = models.IntegerField(default=65)
    partner_height_min = models.IntegerField(help_text="Height in centimeters", default=150)
    partner_height_max = models.IntegerField(help_text="Height in centimeters", default=200)
    partner_religion_preference = models.CharField(max_length=200, blank=True)
    partner_education_preference = models.CharField(max_length=200, blank=True)
    partner_occupation_preference = models.CharField(max_length=200, blank=True)
    other_preferences = models.TextField(blank=True)
    
    # Status and visibility
    is_visible = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def get_absolute_url(self):
        return reverse('view_profile', args=[str(self.id)])
    
    def age(self):
        import datetime
        today = datetime.date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))