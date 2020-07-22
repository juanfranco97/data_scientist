import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    custom_settings = {
        'FEED_URI': 'quotes.json',
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

    def parse_only_quotes(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            author = quote.xpath('.//small[@class="author"]/text()').get()
            text = quote.xpath('./span[@class="text"]/text()').get()
            yield {
            'author': author,
            'text': text,
            }
        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback = self.parse_only_quotes) 
       
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
            author = quote.xpath('.//small[@class="author"]/text()').get()
            text = quote.xpath('./span[@class="text"]/text()').get()
            yield {
            'author': author,
            'text': text,
            }
        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback = self.parse_only_quotes)