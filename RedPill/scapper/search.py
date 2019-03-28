import requests
from bs4 import BeautifulSoup


class Search:
    """
        Scrap the data from target website
    """


    HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'datadome=***LE VOTRE***',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/68.0.3440.106 Safari/537.36'}

    def __init__(self, category, location, postal_code, furnished, page):
        self.category = category
        self.location = location
        self.postal_code = postal_code
        self.furnished = furnished
        self.page = page
        self.url_prefix = "https://www.leboncoin.fr/recherche/?"
        self.url_query = "category=" + category + "&" + "location=" + location + "_" + postal_code + "&" \
                         + "furnished=" + furnished + "&" + "page=" + page

    def request_html(self):
        with requests.Session() as s:
            s.headers = self.HEADERS
            s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
            html = s.get(self.url_prefix + self.url_query).text
            soup = BeautifulSoup(html, "lxml")
            for item in soup.findAll("a", {"class": "clearfix trackable"}):
                print(item)

# s = Search("10", "Clamart", "92140", "1", "1")
# s.request_html()