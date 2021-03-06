# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


class ArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    description = Field()
    link = Field()
    time = Field()
    author = Field()
    pass
class WechatArticleItem(scrapy.Item):
    title = Field()
    link = Field()
    pass
        
