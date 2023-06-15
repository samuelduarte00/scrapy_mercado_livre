import scrapy


class MlSpider(scrapy.Spider):
    name = 'ml'

    start_urls = ['https://www.mercadolivre.com.br/ofertas?page=1']

    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="promotion-item max"]'):
            price = i.xpath(
                './/div[@class="andes-money-amount-combo__main-container"]//span//span[3]//text()').getall()
            title = i.xpath(
                './/p[@class="promotion-item__title"]//text()').get()
            link = i.xpath(
                './/a/@href').get()

            yield {
                'Preço': price,
                'Produto': title,
                'Link': link
            }

        next_page = response.xpath(
            '//a[contains(@title, "Próxima")]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

# para rodar scrapy crawl ml -o pagination.json
