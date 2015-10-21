# -*- coding: utf-8 -*-
import scrapy
import re
import os
import sys

from scrapy.selector import Selector


class ContinenteSpider(scrapy.Spider):
    name = "continente"
    
    def __init__(self, code=''):
        self.start_urls = ['http://www.continente.pt/pt-pt/public/Pages/searchresults.aspx?k=%s' % code]
        self.allowed_domains = ["continente.pt"]
        

    def parse(self, response):
        sel = Selector(response)
        continewnte_result = sel.xpath('//div[@class = "pricePerUnit"]/text()').extract()
        print continewnte_result[0]    