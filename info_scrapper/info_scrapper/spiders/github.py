import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from info_scrapper.items import companyItem
class GithubSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ["github.com"]
    start_urls = [
        "https://github.com/hxu296/leetcode-company-wise-problems-2022"]
    custom_settings = {
        "FEED_URI": "companies.json",
        "FEED_FORMAT": "json",
    }
    #hello world
    def parse(self, response):
        company = companyItem()
        companies= response.xpath(
            "//a[@data-targets='readme-toc.entries']/text()").getall()
        index=2
        for table in response.xpath("//table"):
            company['name']=companies[index]
            index+=1
            company['questions'] = []
            for row in table.xpath(".//tbody//tr"):
                questionSet=[]
                for col in row.xpath(".//td//a[@rel='nofollow']"):
                    questionSet.append(col.xpath(".//@href").get())
                    questionSet.append(col.xpath(".//text()").get())
                company['questions'].append(questionSet)
            yield company
        return company
