from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from profiles.models import Profile

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please create your profile.')
            login(request, user)
            return redirect('create_profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard_view(request):
    try:
        profile = request.user.profile
        profile_complete = True
    except Profile.DoesNotExist:
        profile_complete = False
    
    return render(request, 'accounts/dashboard.html', {
        'profile_complete': profile_complete
    })