import re
import  scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.selector import Selector
from poem_catch.items import PoemCatchItem

class MySpider(scrapy.Spider):
    name = "poem"
    start_url = "https://so.gushiwen.org/gushi/tangshi.aspx"
    url_head = "https://so.gushiwen.org"

    def start_requests(self):
        yield Request(self.start_url, self.parse)

    def parse(self, response):
        urls = []
        soup = BeautifulSoup(response.text, "lxml").find_all("div", class_="cont")[1]
        for s in soup.find_all('a'):
            urls.append(s['href'])
        # sel = Selector(response).xpath("/html/body/div[3]/div[2]/div[1]/div[2]")
        print(urls)
