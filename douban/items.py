# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    '''
    # define the fields for your item here like:
    # name = scrapy.Field()
    #用户id
    user_id = scrapy.Field()

    #想读数量
    user_read_amount = scrapy.Field()
    #已读正在读数量
    user_readed_amount = scrapy.Field()
    #想看数量
    user_watch_amount = scrapy.Field()
    #看过数量
    user_watched_amount = scrapy.Field()

    #书籍id
    book_id = scrapy.Field()
    #书名
    book_name = scrapy.Field()
    #书籍评分
    book_score = scrapy.Field()
    #书籍用户评分
    book_user_score = scrapy.Field()
    #用户标记时间
    book_user_time = scrapy.Field()

    #电影id
    movie_id = scrapy.Field()
    #电影名
    movie_name = scrapy.Field()
    #电影评分
    movie_score = scrapy.Field()
    #电影上映时间
    movie_update_time = scrapy.Field()
    #电影用户评分
    movie_user_score = scrapy.Field()
    #用户标记时间
    movie_mark_time = scrapy.Field()
    '''

    #测试用
    title = scrapy.Field()  # 电影名字
    movieInfo = scrapy.Field()  # 电影的描述信息，包括导演、主演、电影类型等等
    star = scrapy.Field()  # 电影评分
    quote = scrapy.Field()  # 电影中最经典或者说脍炙人口的一句话



