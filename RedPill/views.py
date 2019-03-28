from django.shortcuts import render
from .forms import LocationSearchForm

def search(request):
    if request.method == 'POST':
        location_search_form = LocationSearchForm(request.POST)
        if location_search_form.is_valid():
            return render(request, 'search_progress.html')
    else:
        location_search_form = LocationSearchForm()
    return render(request, 'search.html', {'location_search_form': location_search_form})

def search_progress(request):
    return render(request, 'search_progress.html')