import scrapy
from scrapy_splash import SplashRequest
import time
from ..items import FlatItem


class FotoCasaSpider(scrapy.Spider):
    name = "fotocasa"
    start_urls = [
        "https://www.fotocasa.es/es/alquiler/viviendas/barcelona-capital/todas-las-zonas/l?conservationStatusIds=0&constructionTypeIds=1%2C2&maxPrice=1300&minRooms=3&minSurface=60&sortType=publication"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        # url = response.css("div.quote span.text::text").extract()
        # url = response.css("title").extract()
        # url = response.css("article.re-CardPackMinimal a title").extract()

        # TODO: It doesn't charge all the data (javascript-time)
        # TODO: Iterate for each class where you want to extract its data
        # tittle = response.css(".re-CardTitle").xpath("string()").extract()
        # description = response.css(".re-CardDescription-text::text").extract()
        # price = response.css(".re-CardPrice::text").extract()
        # basic_features = response.css(".re-CardFeatures-feature::text").extract()
        # url = response.css("article.re-CardPackMinimal > a::attr(href)").extract()
        # TODO: Only charge the first image you need to work with javascript
        # img = response.css("article.re-CardPackMinimal > a > div > div > div > ul > li > img::attr(src)").extract()

        items = FlatItem()

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

# //*[@id="App"]/div[1]/div[3]/main/div/div[2]/section/article[1]/a
# article.re-CardPackMinimal:nth-child(1) > a:nth-child(1)
