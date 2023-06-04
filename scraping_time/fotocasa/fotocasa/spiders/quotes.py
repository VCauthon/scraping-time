import scrapy
import time
from ..items import QuotesItems

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):

        items = QuotesItems()

        # Goes throw every tag with the class quote
        for quotes in response.css('div.quote'):

            # Extracts the iterated quotes
            items["text"] = quotes.css('.text::text').extract()[0]\
                .replace('“', '')\
                .replace('”', '')\
                .replace("'", "")
            items["author"] = quotes.css('.author::text').extract()[0]
            items["url_author"] = quotes.css(
                'div.quote > span > a::attr(href)').extract()[0]
            items["tags"] = quotes.css('.tag::text').extract()[0]

            yield items
        # yield {"text": text, "autor": autor, 'url_autor': url_autor}

        # if exists goes to the next page
        next_page = response.css(".next a::attr(href)").get()
        if next_page is not None:
            time.sleep(2)  # Sleeps a while to avoid being banned
            yield response.follow(next_page, callback=self.parse)
