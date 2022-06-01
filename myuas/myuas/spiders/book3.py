import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes31"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel-astral-pet-store/chapter-1/',
            'https://www.worldnovel.online/novel-astral-pet-store/chapter-2/',
            'https://www.worldnovel.online/novel-astral-pet-store/chapter-3/',
            'https://www.worldnovel.online/novel-astral-pet-store/chapter-4/',
            'https://www.worldnovel.online/novel-astral-pet-store/chapter-5/',
            'https://www.worldnovel.online/novel-astral-pet-store/chapter-6/',
            'https://www.worldnovel.online/novel-astral-pet-store/chapter-7/',
            'https://www.worldnovel.online/novel-astral-pet-store/chapter-8/',
            'https://www.worldnovel.online/novel-astral-pet-store/chapter-9/',
            'https://www.worldnovel.online/novel-astral-pet-store/chapter-10/',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }