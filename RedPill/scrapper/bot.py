from ..celery import app
from .search import Search
import jsonpickle

class LbcBot:

    def __init__(self, location_search_form):
        self.URL_queue = []
        self.form = location_search_form
        if self.form is not None:
            self.url_prefix = "https://www.leboncoin.fr/recherche/?"
            self.url_query = "category=" + "10" + \
                             "&locations=" + self.form.cleaned_data["city"] + "_" + self.form.cleaned_data["postal_code"] + \
                             "&real_estate_type=" + str(self.form.cleaned_data["real_estate_type"]) + \
                             "&furnished=" + str(self.form.cleaned_data["furnished"]*1) + \
                             "&price=" + str(self.form.cleaned_data["min_price"]) + "-" + str(self.form.cleaned_data["max_price"]) + \
                             "&rooms=" + str(self.form.cleaned_data["min_rooms"]) + "-" + str(self.form.cleaned_data["max_rooms"]) + \
                             "&square=" + str(self.form.cleaned_data["min_square"]) + "-" + str(self.form.cleaned_data["max_square"]) + \
                             "&page="

    def run(self):
        # query le_bon_coin with form criteria
        search = Search(self.url_prefix, self.url_query + "1")
        html = search.request_html()
        print(html)

@app.task
def run_lbc_bot(json_location_search_form):

    form = jsonpickle.decode(json_location_search_form)
    if form is not None:
        print("OK")
        lbc_bot = LbcBot(form)
        lbc_bot.run()
    else:
        print("Location search form is none")