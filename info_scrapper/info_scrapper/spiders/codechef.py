import scrapy
import requests
from bs4 import BeautifulSoup
import json

class CodechefSpider(scrapy.Spider):
    name = "codechef"
    allowed_domains = ["codechef.com"]
    start_urls = ["https://www.codechef.com/api/list/problems?page=7&limit=50&sort_by=difficulty_rating&sort_order=asc&search=&category=rated&start_rating=0&end_rating=999&topic=&tags=&group=all&="]
    custom_settings={
        "FEED_URI":"codechef.json",
        "FEED_FORMAT":"json",
    }
    def start_requests(self):
        # Define the cookies to send with the request
        cookies = {
            "Cookie":"SESS93b6022d778ee317bf48f7dbffe03173=759139e356ef1a1497969cdde6562fb3"
        }
        # Make the request with the cookies
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=cookies, callback=self.parse)
    def parse(self, response):
        data=json.loads(response.text)
        return data['data']
