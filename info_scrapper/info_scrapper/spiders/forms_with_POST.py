import scrapy
from scrapy.http import FormRequest
from info_scrapper.items import formItem

class FormsSpider(scrapy.Spider):
    name = "forms with post"
    allowed_domains = ["pythonscraping.com"]
    # start_urls = generatestart_urls()
    custom_settings={
        "FEED_URI":"and.json",
        "FEED_FORMAT":"json",
    }

    def start_requests(self):
        names=["codechef","codeforces","hackerearth","hackerrank","spoj"]
        quests=["practice","contests","challenges","problems","questions"]
        for i in range(len(names)):
            print({"name":names[i],"quest":quests[i]})
            yield FormRequest('https://pythonscraping.com/linkedin/formAction2.php',
            formdata={'name':names[i],'quest':quests[i],'color':'red'}
            ,callback=self.parse)
    
    def parse(self, response):
        return {'text':response.xpath('//div[@class="wrapper"]//text()').get()}
