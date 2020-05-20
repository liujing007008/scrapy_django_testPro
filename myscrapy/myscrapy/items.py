# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import scrapy
#
#
# class MyscrapyItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
#

from scrapy_djangoitem import DjangoItem
from save_app.models import My_save_model


class MyscrapyItem(DjangoItem):
    django_model = My_save_model  # 注意这里不要有小括号，因为我们不是调用方法，而只是单纯的把函数名传递过去

