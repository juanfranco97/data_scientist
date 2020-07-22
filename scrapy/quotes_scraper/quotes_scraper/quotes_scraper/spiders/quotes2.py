import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes2'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    custom_settings = {
        'FEED_URI': 'quotes2.json',
        'FEED_FORMAT': 'json',
        'CONCURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['juanfranco1997mi@gmail.com'],
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'Franco97',
        'FEED_EXPORT_ENCODING': 'utf-8'
        #'FEED_URI': 'quotes.csv',
        #'FEED_FORMAT': 'csv',
    }

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        top_tags = response.xpath('//div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()
        top = getattr(self, 'top', None) # if is top in this spider, save the value in top else top = None
        if top:
            top = int(top)
            top_tags = top_tags[:top]
        yield {
            'title': title,
            'top_tags': top_tags,
        }
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))