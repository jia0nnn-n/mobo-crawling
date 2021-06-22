import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mobo.items import MoboItem


class MobospiderSpider(CrawlSpider):
    name = 'mobo-sales'
    allowed_domains = ['www.mo-bo.com.tw']

    # 進入某一檔「顯瘦這樣穿．均一價$590」
    start_urls = ['https://www.mo-bo.com.tw/PDSale.asp?pi=09990727']

    # 抓「裡面的商品」、以及「該商品的搭配」
    rules = (
        Rule(LinkExtractor(allow=r'https://www.mo-bo.com.tw/PDContent'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):

        print('\n\n\n', response.url, '-----------------------------------')

        return
