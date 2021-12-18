import scrapy
from musinsa_crawler.items import MusinsaCrawlerItem

class Spider(scrapy.Spider):

    # user agent 설정(403)
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
        }
    }

    name = "MusinsaOuter"
    allow_domain = ["musinsa.com"]
    start_urls = ["https://search.musinsa.com/ranking/best?mainCategory=002"]

    def parse(self, response):
        # 전체 page 개수 얻어오기
        total_page = response.xpath('//*[@id="goodsRankForm"]/div[2]/div[2]/div[2]/span[8]/span[1]/text()')[0].extract()
        total_page = int(total_page)

        for page in range(1, total_page + 1):
            link = "https://search.musinsa.com/ranking/best?mainCategory=002&page={}".format(page)
            yield scrapy.Request(link, callback=self.page_content)

    def page_content(self, response):
        item_ids = response.xpath('//*[@id="goodsRankList"]/li/@data-goods-no').extract()
        item_titles = response.xpath('//*[@id="goodsRankList"]/li/div[3]/div[2]/p//@title').extract()
        item_titles = list(map(lambda title: title.strip(), item_titles))
        item_prices = response.xpath('//*[@id="goodsRankList"]/li//p[@class="price"]/text()').extract()
        item_prices = list(map(lambda x: x.strip(), item_prices))
        item_prices = list(filter(lambda x: x != '', item_prices))

        item = MusinsaCrawlerItem()

        for item_id, item_title, item_price in zip(item_ids, item_titles, item_prices):
            item['item_id'] = item_id
            item['item_title'] = item_title
            item['item_price'] = int(item_price.replace(",","").replace("원",""))

            yield item

