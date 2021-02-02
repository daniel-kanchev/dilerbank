import scrapy
from scrapy.loader import ItemLoader
from dilerbank.items import Article
from itemloaders.processors import TakeFirst


class DilerSpider(scrapy.Spider):
    name = 'diler'
    start_urls = ['https://www.dilerbank.com.tr/']

    def parse(self, response):
        with open('response.html', 'wb') as f:
            f.write(response.body)

        links = response.xpath('//div[@class="fadeOut owl-carousel owl-theme"]/div[@class="item"]/a/@href') \
            .getall()

        print(links)
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h1/text()').get()
        content = " ".join(response.xpath('//div[@class="content-container"]//text()').getall())

        item.add_value('title', title)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
