from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from profiles.models import Profile
from django.db.models import Q
import datetime

@login_required
def search_view(request):
    form = SearchForm(request.GET or None)
    results = Profile.objects.none()
    
    if form.is_valid() and request.GET:
        results = Profile.objects.filter(is_visible=True).exclude(user=request.user)
        
        # Apply filters
        if form.cleaned_data.get('age_min'):
            max_dob = datetime.date.today() - datetime.timedelta(days=365*form.cleaned_data['age_min'])
            results = results.filter(date_of_birth__lte=max_dob)
        
        if form.cleaned_data.get('age_max'):
            min_dob = datetime.date.today() - datetime.timedelta(days=365*form.cleaned_data['age_max'])
            results = results.filter(date_of_birth__gte=min_dob)
        
        if form.cleaned_data.get('gender'):
            results = results.filter(gender=form.cleaned_data['gender'])
        
        if form.cleaned_data.get('marital_status'):
            results = results.filter(marital_status=form.cleaned_data['marital_status'])
        
        if form.cleaned_data.get('religion'):
            results = results.filter(religion__icontains=form.cleaned_data['religion'])
        
        if form.cleaned_data.get('mother_tongue'):
            results = results.filter(mother_tongue__icontains=form.cleaned_data['mother_tongue'])
        
        if form.cleaned_data.get('country'):
            results = results.filter(country__icontains=form.cleaned_data['country'])
        
        if form.cleaned_data.get('state'):
            results = results.filter(state__icontains=form.cleaned_data['state'])
        
        if form.cleaned_data.get('city'):
            results = results.filter(city__icontains=form.cleaned_data['city'])
        
        if form.cleaned_data.get('education'):
            results = results.filter(education__icontains=form.cleaned_data['education'])
        
        if form.cleaned_data.get('occupation'):
            results = results.filter(occupation__icontains=form.cleaned_data['occupation'])
    
    return render(request, 'search/search_results.html', {
        'form': form,
        'results': results,
        'is_search': bool(request.GET)
    })