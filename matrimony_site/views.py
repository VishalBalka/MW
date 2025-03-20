from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm  # Create this form

def home(request):
    return render(request, 'matrimony_app/home.html')

@login_required
def profile_view(request, username):
    profile = UserProfile.objects.get(user__username=username)
    return render(request, 'matrimony_app/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileFofrom django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm  # Create this form

def home(request):
    return render(request, 'matrimony_app/home.html')

@login_required
def profile_view(request, username):
    profile = UserProfile.objects.get(user__username=username)
    return render(request, 'matrimony_app/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile = UserProfile.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'matrimony_app/profile_edit.html', {'form': form})

@login_required
def search_profiles(request):
    # Implement search logic based on criteria
    profiles = UserProfile.objects.all()  # Filter based on search parameters
    return render(request, 'matrimony_app/search.html', {'profiles': profiles})rm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view', username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'matrimony_app/profile_edit.html', {'form': form})

@login_required
def search_profiles(request):
    # Implement search logic based on criteria
    profiles = UserProfile.objects.all()  # Filter based on search parameters
    return render(request, 'matrimony_app/search.html', {'profiles': profiles})