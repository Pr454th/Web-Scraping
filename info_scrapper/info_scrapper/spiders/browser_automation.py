#automation not working, try to fix it

import scrapy
import time
from scrapy.selector import Selector
from selenium import webdriver

class BrowserAutomationSpider(scrapy.Spider):
    name = "browser_automation"
    allowed_domains = ["cnn.com"]
    start_urls = ["http://example.com"]

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r"/home/prasath/Desktop/Projects/Web-Scraping/info_scrapper/info_scrapper/spiders/Drivers/geckodriver")

    def parse(self, response):
        self.driver.get(response.url)

        # Wait for the page to load
        self.driver.implicitly_wait(10)

        # Extract data using Selenium and XPath
        sel = Selector(text=self.driver.page_source)
        data = sel.xpath("//h1/text()").extract_first()

        # Close the browser
        self.driver.quit()

        # Return the scraped data
        yield {"data": data}

