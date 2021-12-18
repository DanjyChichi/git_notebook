import scrapy
from musinsa_best.items import CrawlerItem

class Spider(scrapy.Spider):
    name = "MusinsaOuterRank"
    allow_domain = ["musinsa.com"]
    start_urls = ["https://search.musinsa.com/ranking/best?mainCategory=002"]
    
    def parse(self, response):
        # 전체 page 개수 얻어오기
        total_page = response.xpath('//*[@id="goodsRankForm"]/div[2]/div[2]/div[2]/span[8]/span[1]/text()')[0].extract()
        total_page = int(total_page)
        
        for page in range(1, total_page+1):
            link = "https://search.musinsa.com/ranking/best?mainCategory=002&page={}".format(page)
            yield scrapy.Request(link, callback=self.page_content)
    
    def page_content(self, response):
        
        item = CrawlerItem()
        
        links = response.xpath('//*[@id="goodsRankList"]/li/div[3]/div[1]/a/@href').extract()
        goods_ids = response.xpath('//*[@id="goodsRankList"]/li/@data-goods-no').extract()
        titles = response.xpath('//*[@id="goodsRankList"]/li/div[3]/div[2]/p[3]/a/text()').extract()
        brands = response.xpath('//*[@id="goodsRankList"]/li/div[3]/div[2]/p[2]/a/text()').extract()
        # 가격이 잘 안들어가는 버그가 있음. 해결 ㄱㄱ
        product_prices = response.xpath('//*[@id="goodsRankList"]/li[6]/div[3]/div[2]/p[3]/text()').extract()
        star_counts = response.xpath('//*[@id="goodsRankList"]/li/div[3]/div[2]/p[5]/span[2]/text()').extract()
        
        for link, goods_id, product_price, star_count, title, brand in zip(links, goods_ids, product_prices, star_counts, titles, brands):
            
            item['link'] = link.strip()
            item['title'] = title.strip().replace(",", "")
            item['brand'] = brand.strip().replace(",", "")
            item['goods_id'] = goods_id.strip()
            item['product_price'] = product_price.strip()
            item['star_count'] = star_count.strip()
            
            yield item
