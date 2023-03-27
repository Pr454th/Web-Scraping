import scrapy
from info_scrapper.items import playerItem

class PlayersSpider(scrapy.Spider):
    name = "players"
    allowed_domains = ["players.com"]
    start_urls = ["https://www.espncricinfo.com/cricketers/quinton-de-kock-379143",
    "https://www.espncricinfo.com/cricketers/johnson-charles-333066",
    "https://www.espncricinfo.com/cricketers/kyle-abbott-297583",
    "https://www.espncricinfo.com/cricketers/matthew-breetzke-595267",
    "https://www.espncricinfo.com/cricketers/junior-dala-545467",
    "https://www.espncricinfo.com/cricketers/akila-dananjaya-574178",
    "https://www.espncricinfo.com/cricketers/simon-harmer-432960",
    "https://www.espncricinfo.com/cricketers/jason-holder-391485",
    "https://www.espncricinfo.com/cricketers/christiaan-jonker-222320",
    "https://www.espncricinfo.com/cricketers/heinrich-klaasen-436757",
    "https://www.espncricinfo.com/cricketers/dilshan-madushanka-793007",
    "https://www.espncricinfo.com/cricketers/keshav-maharaj-267724",
    "https://www.espncricinfo.com/cricketers/kyle-mayers-348056",
    "https://www.espncricinfo.com/cricketers/wiaan-mulder-698189",
    "https://www.espncricinfo.com/cricketers/keemo-paul-677081",
    "https://www.espncricinfo.com/cricketers/dwaine-pretorius-327830",
    "https://www.espncricinfo.com/cricketers/prenelan-subrayen-437438",
    "https://www.espncricinfo.com/cricketers/reece-topley-461632",
    "https://www.espncricinfo.com/cricketers/hardus-viljoen-375126"]
    custom_settings={
        "FEED_URI":"Durban's Super Giants squad.json",
        "FEED_FORMAT":"json",
    }
    def parse(self, response):
        player = playerItem()
        player['name']=""
        player['nationalteam']=""
        player['battingStyle']=""
        player['bowlingStyle']=""
        player['playingRole']=""
        player['image']=""
        fields=response.xpath("//p[@class='ds-text-tight-m ds-font-regular ds-uppercase ds-text-typo-mid3']//text()").getall()
        details=response.xpath("//span[@class='ds-text-title-s ds-font-bold ds-text-typo']//h5//text()").getall()
        player['nationalteam']=response.xpath("//span[@class='ds-text-comfortable-s']//text()").get()
        player['image']=response.xpath("//meta[@property='og:image']/@content").get()
        print(details)
        print(fields)
        print(player['nationalteam'])
        print(player['image'])
        for i in range(len(fields)):
            print(fields[i],details[i])
            if(fields[i]=="Full Name"):
                player['name']=details[i]
            elif(fields[i]=="Batting Style"):
                player['battingStyle']=details[i]
            elif(fields[i]=="Bowling Style"):
                player['bowlingStyle']=details[i]
            elif(fields[i]=="Playing Role"):
                player['playingRole']=details[i]
            else:
                print("hello world")
        yield player