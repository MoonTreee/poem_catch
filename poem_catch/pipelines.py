# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import scrapy


class PoemCatchPipeline(object):
    def process_item(self, item, spider):
        line = item['name'] + '\t' + item['dynasty']+ '\t' +item['writer']+ '\t' +item['content']+ '\t' +item['type']
        line = line.replace("\n", '') + "\n"
        file = open("poem.txt", "a+")
        file.writelines(line)
        return item

