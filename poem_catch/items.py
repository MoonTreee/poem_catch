# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PoemCatchItem(scrapy.Item):
    # 诗词题目
    name = scrapy.Field()
    # 诗词内容
    content = scrapy.Field()
    # 作者
    writer = scrapy.Field()
    # 朝代
    dynasty = scrapy.Field()
    # 类别
    type = scrapy.Field()
    pass
