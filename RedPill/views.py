from django.shortcuts import render, redirect
import jsonpickle
from .forms import LocationSearchForm, IsRelevantForm
from .scrapper.bot import run_lbc_bot
from .utils.dashboard_utils import *

def search(request):
    if request.method == 'POST':
        location_search_form = LocationSearchForm(request.POST)
        if location_search_form.is_valid():
            json_form = jsonpickle.encode(location_search_form)
            run_lbc_bot.delay(json_form)
            return redirect("/search/picking/" + location_search_form.cleaned_data["postal_code"] + "/")
        else:
            print("location_search_form is NOT valid")
    else:
        location_search_form = LocationSearchForm()
    return render(request, 'search.html', {'location_search_form': location_search_form})

def search_results(request, postal_code):
    is_relevant_form = IsRelevantForm(request.POST)
    if is_relevant_form.is_valid():
        location = Location.objects.get(url=is_relevant_form.cleaned_data["url"])
        location.is_relevant = is_relevant_form.cleaned_data["is_relevant"]
        location.price = is_relevant_form.cleaned_data["real_price"]
        location.has_been_seen = True
        location.save()

    locations = Location.objects.filter(postal_code=postal_code, has_been_seen=False)
    if len(locations) > 0:
        location = locations[0]
        location.images = location.images.split("|")

        is_relevant_form = IsRelevantForm()
        return render(request, 'search_results.html', {'location': location,
                                                       'is_relevant_form': is_relevant_form})
    else:
        return render(request, 'search_results.html')


def dashboard(request, postal_code):
    mean_price_vs_square = get_mean_price_by_square_from_postal_code(postal_code)
    locations = Location.objects.filter(postal_code=postal_code, has_been_seen=True, is_relevant=True)
    print(mean_price_vs_square)
    if len(locations) > 0:
        city = locations[0].city

        locations_json = []
        for location in locations:
            temp = {}
            temp["y"] = location.price
            temp["x"] = location.square
            locations_json.append(temp)

        return render(request, 'dashboard.html', {'locations': locations_json,
                                                  'city': city,
                                                  'mean_price_vs_square': mean_price_vs_square})