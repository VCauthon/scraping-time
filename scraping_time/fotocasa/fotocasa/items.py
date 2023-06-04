# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlatItem(scrapy.Item):

    # Contact data
    url = scrapy.Field()
    title = scrapy.Field()
    phone = scrapy.Field()
    announcement_date = scrapy.Field()

    # Critical data
    price = scrapy.Field()
    rooms = scrapy.Field()
    size = scrapy.Field()
    photos = scrapy.Field()
    map_location = scrapy.Field()

    # Extra data
    floor = scrapy.Field()
    bathrooms = scrapy.Field()
    balcony = scrapy.Field()
    furnished = scrapy.Field()


class QuotesItems(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    author = scrapy.Field()
    url_author = scrapy.Field()
    tags = scrapy.Field()
