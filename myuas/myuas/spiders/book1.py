import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes12"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/martial-god-asura/martial-god-asura-chapter-1-indonesian-language/',
            'https://www.worldnovel.online/martial-god-asura/martial-god-asura-chapter-2-indonesian-language/',
            'https://www.worldnovel.online/martial-god-asura/martial-god-asura-chapter-3-the-indonesian-language/',
            'https://www.worldnovel.online/martial-god-asura/martial-god-asura-chapter-4-indonesian-language/',
            'https://www.worldnovel.online/martial-god-asura/martial-god-asura-chapter-5-indonesian-language/',
            'https://www.worldnovel.online/martial-god-asura/martial-god-asura-chapter-6-indonesian-language/',
            'https://www.worldnovel.online/martial-god-asura/martial-god-asura-chapter-7-indonesian-language/',
            'https://www.worldnovel.online/martial-god-asura/martial-god-asura-chapter-8-indonesian-language/',
            'https://www.worldnovel.online/martial-god-asura/martial-god-asura-chapter-9-i-indonesian/',
            'https://www.worldnovel.online/martial-god-asura/martial-god-asura-chapter-10-indonesian-language/',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }