from django.shortcuts import render
import jsonpickle
from .forms import LocationSearchForm
from .scrapper.bot import run_lbc_bot

def search(request):
    if request.method == 'POST':
        location_search_form = LocationSearchForm(request.POST)
        if location_search_form.is_valid():
            json_form = jsonpickle.encode(location_search_form)
            run_lbc_bot.delay(json_form)
            return render(request, 'search_progress.html')
    else:
        location_search_form = LocationSearchForm()
    return render(request, 'search.html', {'location_search_form': location_search_form})

def search_progress(request):
    return render(request, 'search_progress.html')