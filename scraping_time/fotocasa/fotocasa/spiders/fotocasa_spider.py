import scrapy


class FotoCasaSpider(scrapy.Spider):
    name = "fotocasa"
    start_urls = [
        # "https://www.fotocasa.es/es/alquiler/viviendas/barcelona-capital/"
        # "todas-las-zonas/l?conservationStatusIds=0&constructionTypeIds=1%"
        # "2C2&maxPrice=1300&minRooms=3&minSurface=60&sortType=publication"
        # "Date",
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # url = response.css("div.quote span.text::text").extract()
        url = response.css("title").extract()
        # url = response.css("article.re-CardPackMinimal a title").extract()
        yield {"url": url}


# //*[@id="App"]/div[1]/div[3]/main/div/div[2]/section/article[1]/a
# article.re-CardPackMinimal:nth-child(1) > a:nth-child(1)
