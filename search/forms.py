from django import forms
from profiles.models import Profile

class SearchForm(forms.Form):
    GENDER_CHOICES = [('', 'Any')] + Profile.GENDER_CHOICES
    MARITAL_STATUS_CHOICES = [('', 'Any')] + Profile.MARITAL_STATUS_CHOICES
    
    age_min = forms.IntegerField(required=False, min_value=18, max_value=80, label="Min Age")
    age_max = forms.IntegerField(required=False, min_value=18, max_value=80, label="Max Age")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS_CHOICES, required=False)
    religion = forms.CharField(required=False)
    mother_tongue = forms.CharField(required=False)
    country = forms.CharField(required=False)
    state = forms.CharField(required=False)
    city = forms.CharField(required=False)
    education = forms.CharField(required=False)
    occupation = forms.CharField(required=False)