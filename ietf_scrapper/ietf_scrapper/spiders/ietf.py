import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        # title=response.css("span.title::text").get()
        title=response.xpath("//span[@class='title']/text()").get()
        subheading=response.xpath("//span[@class='subheading']/text()").getall()
        address=response.xpath("//span[@class='address']/text()").get()
        phone=response.xpath("//span[@class='phone']/text()").get()
        email=response.xpath("//span[@class='email']/text()").get()
        description=response.xpath("//meta[@name='DC.Description.Abstract']/@content").get()
        return {"title":title,"subheading":subheading,"address":address,"phone":phone,"email":email,"description":description}
