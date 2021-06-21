import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MobospiderSpider(CrawlSpider):
    name = 'mobospider'
    allowed_domains = ['www.mo-bo.com.tw']

    # 進入點
    start_urls = ['http://www.mo-bo.com.tw/']

    # 抓「特價」相關的頁面
    rules = (
        Rule(LinkExtractor(allow=r'https://www.mo-bo.com.tw/PDSale'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
