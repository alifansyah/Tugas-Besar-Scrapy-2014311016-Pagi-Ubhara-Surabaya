import scrapy


class QuotesSpider(scrapy.Spider):
    name = "buku4"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel-rkr-id/prologue-chapter-1/',
            'https://www.worldnovel.online/novel-rkr-id/chapter-2/',
            'https://www.worldnovel.online/novel-rkr-id/chapter-3/',
            'https://www.worldnovel.online/novel-rkr-id/chapter-4/',
            'https://www.worldnovel.online/novel-rkr-id/chapter-5/',
            'https://www.worldnovel.online/novel-rkr-id/chapter-6/',
            'https://www.worldnovel.online/novel-rkr-id/chapter-7/',
            'https://www.worldnovel.online/novel-rkr-id/chapter-8/',
            'https://www.worldnovel.online/novel-rkr-id/chapter-9/',
            'https://www.worldnovel.online/novel-rkr-id/chapter-10/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }