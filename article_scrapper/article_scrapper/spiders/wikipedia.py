import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from article_scrapper.items import Article

class WikipediaSpider(CrawlSpider):
    name = "wikipedia"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Kevin_Bacon"]

    rules=[Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'),callback='parse_info',follow=True)]

    # custom settings for this spider
    custom_settings={
        "FEED_URI":"articles.json",
        "FEED_FORMAT":"json",
    }

    def parse_info(self, response):
        article=Article()
        article["title"]=response.xpath("//h1/text()").get() or response.xpath("//h1/i/text()").get()
        article["url"]=response.url
        article["lastUpdated"]=response.xpath("//li[@id='footer-info-lastmod']/text()").get()
        
        return article
        # return {
        #     "title":response.xpath("//h1/text()").get() or response.xpath("//h1/i/text()").get(),
        #     "url":response.url,
        #     "last_edited":response.xpath("//li[@id='footer-info-lastmod']/text()").get(),

        # }
