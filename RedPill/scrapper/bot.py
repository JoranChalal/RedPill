from ..celery import app
from .search import Search
import jsonpickle
import time

class LbcLocationScrapperBot:

    def __init__(self, location_search_form):
        self.URL_queue = []
        self.form = location_search_form
        if self.form is not None:
            self.url_prefix = "https://www.leboncoin.fr/recherche/?"
            if self.form.cleaned_data["furnished"]:
                furnished  = 1
            else:
                furnished = 2
            self.url_query = "category=" + "10" + \
                             "&locations=" + self.form.cleaned_data["city"] + "_" + self.form.cleaned_data["postal_code"] + \
                             "&real_estate_type=" + str(self.form.cleaned_data["real_estate_type"]) + \
                             "&furnished=" + str(furnished) + \
                             "&price=" + str(self.form.cleaned_data["min_price"]) + "-" + str(self.form.cleaned_data["max_price"]) + \
                             "&rooms=" + str(self.form.cleaned_data["min_rooms"]) + "-" + str(self.form.cleaned_data["max_rooms"]) + \
                             "&square=" + str(self.form.cleaned_data["min_square"]) + "-" + str(self.form.cleaned_data["max_square"]) + \
                             "&page="

    def run(self):
        page_increment = 0
        # query le_bon_coin with form criteria
        # while until there is no further page available
        href_list = []
        while len(href_list) > 0 or page_increment == 0:
            # re-populate href_list with new page (if there is data)
            page_increment += 1
            print("Page " + str(page_increment))
            time.sleep(10)
            search = Search(self.url_prefix, self.url_query + str(page_increment))
            html = search.request_html()
            self.URL_queue = self.URL_queue + href_list
            href_list = search.get_locations_href(html)
            print(href_list)

        print("DONE")


@app.task
def run_lbc_bot(json_location_search_form):
    form = jsonpickle.decode(json_location_search_form)
    if form is not None:
        lbc_bot = LbcLocationScrapperBot(form)
        lbc_bot.run()