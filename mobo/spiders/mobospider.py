import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MobospiderSpider(CrawlSpider):
    name = 'mobospider'
    allowed_domains = ['www.mo-bo.com.tw']

    # 進入某一檔「兩件五折」
    start_urls = ['https://www.mo-bo.com.tw/PDSale.asp?pi=09990707']

    # 抓「裡面的商品」、以及「該商品的搭配」
    rules = (
        Rule(LinkExtractor(allow=r'https://www.mo-bo.com.tw/PDContent'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
