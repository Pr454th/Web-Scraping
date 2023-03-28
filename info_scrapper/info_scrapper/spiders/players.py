import scrapy
from info_scrapper.items import playerItem

import requests
from bs4 import BeautifulSoup
class PlayersSpider(scrapy.Spider):
    name = "players"
    allowed_domains = ["players.com"]
    url="https://www.espncricinfo.com/series/sa20-2022-23-1335268/paarl-royals-squad-1335771/series-squads"
    res=requests.get(url)
    soup=BeautifulSoup(res.content, 'html5lib')
    cricketers=[]
    for a in soup.find_all('a', href=True,class_='ds-inline-flex ds-items-start ds-leading-none'):
        if "/cricketers" in a['href']:
            cricketers.append("https://www.espncricinfo.com"+a['href'])
    start_urls =cricketers
    custom_settings={
        "FEED_URI":"test.json",
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
