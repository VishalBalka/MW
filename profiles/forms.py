from django import forms
from .models import Profile
import datetime

class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(datetime.date.today().year - 80, datetime.date.today().year - 18)
        )
    )
    
    class Meta:
        model = Profile
        exclude = ['user', 'is_featured', 'created_at', 'updated_at']
        widgets = {
            'about_me': forms.Textarea(attrs={'rows': 5}),
            'other_preferences': forms.Textarea(attrs={'rows': 5}),
        }