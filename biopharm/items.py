# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiopharmItem(scrapy.Item):
    # define the fields for your item here
    ticker = scrapy.Field()
    price = scrapy.Field()
    drug = scrapy.Field()
    stage = scrapy.Field()
    catalyst = scrapy.Field()
    note = scrapy.Field()
    
