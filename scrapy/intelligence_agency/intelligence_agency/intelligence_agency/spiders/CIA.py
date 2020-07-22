import scrapy

class SpiderCIA(scrapy.Spider):
    name = 'CIA'
    start_urls = [
        'https://www.cia.gov/library/readingroom/historical-collections'
    ]
    custom_settings = {
        'FEED_URI': 'CIA.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links_declassified = response.xpath('//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').extract()
        for link in links_declassified:
            yield response.follow(link, callback=self.parse_link, meta={'url':response.urljoin(link)})

    def parse_link(self, response):
        link = response.meta['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').extract()
        paragraph = response.xpath('//div[@class="field-item even"]//p[not(@class)]/text()').extract()
        yield {
            'url': link,
            'title': title,
            'body': paragraph
        }
#response.xpath('//a[@href = "special-collections-archive"]/@href').get()


