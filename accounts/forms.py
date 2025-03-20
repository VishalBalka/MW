from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    account_type = forms.ChoiceField(
        choices=[
            ('SELF', 'Self'),
            ('PARENT', 'Parent/Guardian'),
            ('SIBLING', 'Sibling'),
            ('RELATIVE', 'Relative'),
            ('FRIEND', 'Friend'),
        ],
        required=True
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 
                  'password1', 'password2', 'phone_number', 'account_type')
    
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                account_type=self.cleaned_data['account_type']
            )
        
        return user