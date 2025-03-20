from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile
from django.db.models import Q

@login_required
def create_profile_view(request):
    # Check if profile already exists
    try:
        profile = request.user.profile
        return redirect('edit_profile')
    except Profile.DoesNotExist:
        pass
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your profile has been created successfully!')
            return redirect('dashboard')
    else:
        form = ProfileForm()
    
    return render(request, 'profiles/create_profile.html', {'form': form})

@login_required
def edit_profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('create_profile')
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profiles/edit_profile.html', {'form': form})

def view_profile_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    
    # Check if the profile is visible or belongs to the current user
    if not profile.is_visible and (not request.user.is_authenticated or request.user != profile.user):
        messages.error(request, 'This profile is not available.')
        return redirect('home')
    
    return render(request, 'profiles/view_profile.html', {'profile': profile})

@login_required
def profile_list_view(request):
    # Get all visible profiles except the current user's
    profiles = Profile.objects.filter(is_visible=True).exclude(user=request.user)
    
    # Basic filtering based on gender preference (if the user has a profile)
    try:
        user_profile = request.user.profile
        if user_profile.gender == 'M':
            profiles = profiles.filter(gender='F')
        elif user_profile.gender == 'F':
            profiles = profiles.filter(gender='M')
    except Profile.DoesNotExist:
        pass
    
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})