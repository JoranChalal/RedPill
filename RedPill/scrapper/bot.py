from django.core.exceptions import ObjectDoesNotExist
from ..celery import app
from .search import Search
from ..models import Location
import jsonpickle
import time
import random

class LbcLocationScrapperBot:

    def __init__(self, location_search_form):
        self.url_queue = []
        self.form = location_search_form
        if self.form is not None:
            if self.form.cleaned_data["furnished"]:
                furnished  = 1
            else:
                furnished = 2

            self.url_prefix = "https://www.leboncoin.fr"
            self.url_query_pages = "/recherche/?category=" + "10" + \
                             "&locations=" + self.form.cleaned_data["city"] + "_" + self.form.cleaned_data["postal_code"] + \
                             "&real_estate_type=" + str(self.form.cleaned_data["real_estate_type"]) + \
                             "&furnished=" + str(furnished) + \
                             "&price=" + str(self.form.cleaned_data["min_price"]) + "-" + str(self.form.cleaned_data["max_price"]) + \
                             "&rooms=" + str(self.form.cleaned_data["min_rooms"]) + "-" + str(self.form.cleaned_data["max_rooms"]) + \
                             "&square=" + str(self.form.cleaned_data["min_square"]) + "-" + str(self.form.cleaned_data["max_square"]) + \
                             "&page="

    def run(self):
        self.get_all_locations_url()
        self.fill_all_locations_data()

    def get_all_locations_url(self):
        page_increment = 0
        # query le_bon_coin with form criteria
        # while until there is no further page available
        href_list = []
        search = Search()
        while len(href_list) > 0 or page_increment == 0:
            # re-populate href_list with new page (if there is data)
            page_increment += 1
            # time.sleep(1 + random.randint(1, 3))
            html = search.request_html(self.url_prefix, self.url_query_pages + str(page_increment))
            self.url_queue = self.url_queue + href_list
            href_list = search.get_locations_href(html)
            print("Page " + str(page_increment), href_list)

            # for each href in the list, create a Location object and store the url
            # check before if this URL is already in database
            for href in href_list:
                try:
                    location = Location.objects.get(url=href)
                except ObjectDoesNotExist:
                    location = None

                if location is None:
                    location = Location(url=href)
                    location.save()
                    print("Location saved in database")
                else:
                    print("Location already in database")
        search.quit()

    def fill_all_locations_data(self):
        search = Search()
        for href in self.url_queue:
            # time.sleep(1 + random.randint(1, 3))
            try:
                location = Location.objects.get(url=href)
            except ObjectDoesNotExist:
                location = None
            if location is not None:
                print("Filling " + self.url_prefix + href)
                html = search.request_html(self.url_prefix, href)
                location = Search.fill_location_data(html, location)
                location.save()
        search.quit()

@app.task
def run_lbc_bot(json_location_search_form):
    form = jsonpickle.decode(json_location_search_form)
    if form is not None:
        lbc_bot = LbcLocationScrapperBot(form)
        lbc_bot.run()