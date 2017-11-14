# from scrapy.spider import BaseSpider
# from scrapy.selector import HtmlXPathSelector
# from scrapy.contrib.loader import XPathItemLoader
# from scrapy.contrib.loader.processor import Join, MapCompose
# from Scraper_App.items import Dungeon
import scrapy

class Dungeon_Spider(scrapy.Spider):

    name = 'dungeon_spider'
    allowed_domains = ["puzzledragonx.com"]
    start_urls = ["http://www.puzzledragonx.com"]

    def parse(self, response):

        yield {
            'dungeon' : response.xpath('//td[@class = "eventname"]/a/text()').extract()
        }
