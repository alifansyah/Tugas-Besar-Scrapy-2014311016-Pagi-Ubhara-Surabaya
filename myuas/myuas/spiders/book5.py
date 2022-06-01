import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes51"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel-my-disciples-are-all-villains-indo/chapter-1/',
            'https://www.worldnovel.online/novel-my-disciples-are-all-villains-indo/chapter-2/',
            'https://www.worldnovel.online/novel-my-disciples-are-all-villains-indo/chapter-3/',
            'https://www.worldnovel.online/novel-my-disciples-are-all-villains-indo/chapter-4/',
            'https://www.worldnovel.online/novel-my-disciples-are-all-villains-indo/chapter-5/',
            'https://www.worldnovel.online/novel-my-disciples-are-all-villains-indo/chapter-6/',
            'https://www.worldnovel.online/novel-my-disciples-are-all-villains-indo/chapter-7/',
            'https://www.worldnovel.online/novel-my-disciples-are-all-villains-indo/chapter-8/',
            'https://www.worldnovel.online/novel-my-disciples-are-all-villains-indo/chapter-9/',
            'https://www.worldnovel.online/novel-my-disciples-are-all-villains-indo/chapter-10/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }