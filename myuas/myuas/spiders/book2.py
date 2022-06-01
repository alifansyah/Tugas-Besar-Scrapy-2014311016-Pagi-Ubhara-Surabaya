import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes2"

    def start_requests(self):
        urls = [
            'https://www.worldnovel.online/novel-alchemy-emperor-of-the-divine-dao-id-2/aeotdd-chapter-1-indonesian/',
            'https://www.worldnovel.online/novel-alchemy-emperor-of-the-divine-dao-id-2/aeotdd-chapter-2-indonesian/',
            'https://www.worldnovel.online/novel-alchemy-emperor-of-the-divine-dao-id-2/aeotdd-chapter-3-indonesian/',
            'https://www.worldnovel.online/novel-alchemy-emperor-of-the-divine-dao-id-2/aeotdd-chapter-4-indonesian/',
            'https://www.worldnovel.online/novel-alchemy-emperor-of-the-divine-dao-id-2/aeotdd-chapter-5-indonesian/',
            'https://www.worldnovel.online/novel-alchemy-emperor-of-the-divine-dao-id-2/aeotdd-chapter-6-indonesian/',
            'https://www.worldnovel.online/novel-alchemy-emperor-of-the-divine-dao-id-2/aeotdd-chapter-7-indonesian/',
            'https://www.worldnovel.online/novel-alchemy-emperor-of-the-divine-dao-id-2/aeotdd-chapter-8-indonesian/',
            'https://www.worldnovel.online/novel-alchemy-emperor-of-the-divine-dao-id-2/aeotdd-chapter-9-indonesian/',
            'https://www.worldnovel.online/novel-alchemy-emperor-of-the-divine-dao-id-2/aeotdd-chapter-10-indonesian/',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    

    def parse(self, response):
        yield{
            'testing':response.css('#soop > p ::text').extract()
        }