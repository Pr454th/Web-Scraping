import scrapy

def generatestart_urls():
    names=["codechef","codeforces","hackerearth","hackerrank","spoj"]
    quests=["practice","contests","challenges","problems","questions"]
    return ['https://pythonscraping.com/linkedin/formAction.php?name={}&quest={}&color=red'.format(name,quest) for name in names for quest in quests]

class FormsSpider(scrapy.Spider):
    name = "forms"
    allowed_domains = ["pythonscraping.com"]
    start_urls = generatestart_urls()

    def parse(self, response):
        return {'text':response.xpath('//div[@class="wrapper"]//text()').get()}
