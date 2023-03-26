import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news_scrapper.items import companyItem

class GithubSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/hxu296/leetcode-company-wise-problems-2022"]
    custom_settings={
        "FEED_URI":"companies.json",
        "FEED_FORMAT":"json",
    }
    def parse(self, response):
        company=companyItem()
        company["name"]=response.xpath("//a[@role='menuitem']/text()").getall()
        company["questions"]=response.xpath("//a[@rel='nofollow']/@href").getall()
        return company
