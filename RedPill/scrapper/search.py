from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from datetime import datetime

class Search:
    """
        Scrap the data from target website
    """

    HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'datadome=***NEW COOKIE***',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/68.0.3440.106 Safari/537.36'}

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(executable_path=r'/Users/Joran/PycharmProjects/RedPill/geckodriver', options=options)

    def request_html(self, url_prefix, url_query):
        self.driver.get(url_prefix + url_query)
        html = self.driver .execute_script("return document.documentElement.outerHTML")
        soup = BeautifulSoup(html)
        return soup

    def quit(self):
        self.driver.close()
        self.driver.quit()

    @staticmethod
    def get_locations_href(html):
        a = []
        for item in html.findAll("a", {"class": "clearfix trackable"}):
            a.append(item['href'])
        return a

    @staticmethod
    def fill_location_data(html, location):
        location.title = Search.get_location_title(html)
        location.price = Search.get_location_price(html)
        location.date = Search.get_location_date(html)
        return location

    @staticmethod
    def get_location_title(html):
        for item in html.findAll("div", {"data-qa-id": "adview_title"}):
            title = item.h1
            if title != "" and title is not None and title.get_text() != "":
                print("Title :" + title.get_text())
                return title.get_text()

    @staticmethod
    def get_location_price(html):
        for item in html.findAll("div", {"data-qa-id": "adview_price"}):
            price = item.span
            if price != "" and price is not None and price.get_text() != "":
                print("Price :" + price.get_text())
                return price.get_text().split()[0]

    @staticmethod
    def get_location_date(html):
        for item in html.findAll("div", {"data-qa-id": "adview_date"}):
            if item != "" and item is not None and item.get_text() != "":
                print("Date :" + item.get_text())
                return datetime.strptime(item.get_text().split()[0], '%d/%m/%Y').strftime("%Y-%m-%d")