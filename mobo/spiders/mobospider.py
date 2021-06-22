import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mobo.items import MoboItem
from scrapy.pipelines.images import ImagesPipeline


class MobospiderSpider(CrawlSpider):
    name = 'mobo-template'
    allowed_domains = ['pantsevent.mo-bo.com.tw']

    # 「穿搭gallery」
    start_urls = ['http://pantsevent.mo-bo.com.tw/gallery/new']

    # 抓「第一頁」的所有範本
    rules = (
        Rule(LinkExtractor(allow=r'http://pantsevent.mo-bo.com.tw/info'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = MoboItem()
        item['image_urls'] = response.xpath('.//div[@class="pic"]/img/@src').extract()
        yield item
