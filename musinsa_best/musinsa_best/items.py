import scrapy

class CrawlerItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    goods_id = scrapy.Field()
    product_price = scrapy.Field()
    star_count = scrapy.Field()
