import scrapy
from scrapy.loader import ItemLoader
from myproject.items import MyprojectItem

class BookSpider(scrapy.Spider):
    name = 'book'
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for article in response.xpath("//article[@class='product_pod']"):
            loader = ItemLoader(item=MyprojectItem(), selector=article)

            book_name = article.xpath(".//h3/a/@title").get()
            url = article.xpath(".//div[@class='image_container']/a/img/@src").extract_first()
            image_urls = response.urljoin(url)

            loader.add_value('image_urls', image_urls)
            loader.add_value('book_name', book_name)
            yield loader.load_item()
