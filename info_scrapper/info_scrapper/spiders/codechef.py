import scrapy
import requests
from bs4 import BeautifulSoup
import json

class CodechefSpider(scrapy.Spider):
    name = "codechef"
    allowed_domains = ["codechef.com"]
    start_urls = ["http://codechef.com/"]
    custom_settings={
        "FEED_URI":"codechef.csv",
        "FEED_FORMAT":"csv",
    }
    def parse(self, response):
        print("hello world")
        url="https://www.codechef.com/api/list/problems?page=7&limit=50&sort_by=difficulty_rating&sort_order=asc&search=&category=rated&start_rating=0&end_rating=999&topic=&tags=&group=all&="
        cookies = {
            "Cookie":"SESS93b6022d778ee317bf48f7dbffe03173=759139e356ef1a1497969cdde6562fb3"
        }
        res=requests.get(url,cookies=cookies)
        data=json.loads(res.content)
        return data['data']
