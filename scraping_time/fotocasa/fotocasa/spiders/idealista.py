import scrapy
from ..items import FlatItem


class IdealistaSpider(scrapy.Spider):
    name = "idealista"
    allowed_domains = ["www.idealista.com"]
    start_urls = [
        "https://www.idealista.com/areas/alquiler-viviendas/con-precio-hasta_1300,metros-cuadrados-mas-de_60,de-tres-dormitorios,de-cuatro-cinco-habitaciones-o-mas,publicado_ultima-semana/?shape=%28%28ilt%7BFuy_Lmb%40ePmf%40c%5Emn%40gQamAa%7B%40jb%40euClf%40dB%7CW_NzK_z%40kZcyApYsqAhN%7Ci%40nn%40uH%7Eg%40ho%40%7Ct%40h%7E%40pYl%60A%60h%40%7Cx%40XzdB%7EBjkBgNhRe%5Bc%5Eik%40%60N%7D%5BlT%7DWdP%29%29&ordenado-por=fecha-publicacion-desc"]

    # Parses the response received from the start_urls
    def parse(self, response):

        # Creates the object where all the data will be stored
        items = FlatItem()

        # Goes for each announcement
        for anno in response.css('#main-content'):

            # Contact data
            items['title'] = anno.css('.item-link::attr(title)').extract()
            items['url'] = anno.css('.item-link::attr(href)').extract()  # Get the full url
            # items['phone'] = anno.css('').extract()  # https://www.idealista.com/es/ajax/ads/{id-inmueble}/contact-phones
            items['announcement_date'] = anno.css('.item-detail:nth-child(4)::text').extract()

            # Critical data
            items['price'] = anno.css('.h2-simulated::text').extract()
            items['rooms'] = anno.css('.item-detail:nth-child(1)::text').extract()
            items['size'] = anno.css('.item-detail:nth-child(2)::text').extract()
            # items['photos'] = anno.css('').extract()
            # items['map_location'] = anno.css('').extract()

            # Extra data
            items['floor'] = anno.css('.item-detail:nth-child(3)::text').extract()
            # items['bathrooms'] = anno.css('').extract()
            # items['balcony'] = anno.css('').extract()
            # items['furnished'] = anno.css('').extract()

            # Returns the gathered data
            yield items
