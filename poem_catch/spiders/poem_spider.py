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
        yield Request(self.start_url, self.get_url)

    def get_url(self, response):
        soup = BeautifulSoup(response.text, "lxml").find_all("div", class_="cont")[1]
        for s in soup.find_all('a'):
            yield Request(self.url_head + s['href'], self.parse_url)
        # sel = Selector(response).xpath("/html/body/div[3]/div[2]/div[1]/div[2]")

    def parse_url(self, response):
        soup = BeautifulSoup(response.text, "lxml").find('div', class_="sons")
        for s in soup.find_all("span"):
            url =self.url_head + s.find('a')['href']
            yield Request(url, self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        # name = Selector(response).select("/html/body/div[3]/div[1]/div[2]/div[1]/h1")
        name = soup.find("h1",style="font-size:20px; line-height:22px; height:22px; margin-bottom:10px;").get_text()
        content = soup.find("div", class_= "contson").get_text()
        writer = soup.find('p',class_="source").find_all('a')[1].get_text()
        dynasty = soup.find('p',class_="source").find_all('a')[0].get_text()
        type = soup.find("div", class_="tag").get_text().replace("\n", "")
        item = PoemCatchItem()
        item["name"] = name
        item['content'] = content
        item['writer'] = writer
        item['dynasty']= dynasty
        item['type'] = type
        yield item
