#coding:utf-8
"""
爬虫启动方法：通过输入爬虫的name进行仿cmd的方式进行启动
"""
from scrapy import cmdline

crawl_name = 'poem'
cmd = 'scrapy crawl {0}'.format(crawl_name)
cmdline.execute(cmd.split())