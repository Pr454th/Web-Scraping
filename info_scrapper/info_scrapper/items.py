# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class companyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    questions=scrapy.Field()

class playerItem(scrapy.Item):
    name=scrapy.Field()
    nationalteam=scrapy.Field()
    battingStyle=scrapy.Field()
    bowlingStyle=scrapy.Field()
    playingRole=scrapy.Field()
    image=scrapy.Field()
    team=scrapy.Field()