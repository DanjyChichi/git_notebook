import scrapy

class MusinsaCrawlerItem(scrapy.Item):
    item_id    = scrapy.Field()
    item_price = scrapy.Field()
    item_title = scrapy.Field()
