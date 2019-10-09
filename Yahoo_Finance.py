# -*- coding: utf-8 -*-
import scrapy


class YahooFinanceSpider(scrapy.Spider):
    name = 'Yahoo_Finance'
    allowed_domains = ['finance.yahoo.com/']
    start_urls = (
        'http://finance.yahoo.com/gainers',
        )

    def parse(self, response):
        listings = response.xpath('//*[@class="W(100%)"]')
        for listing in listings:
            symbols = listing.xpath('.//*[@class="Fw(600)"]/text()').extract()
            intraday_price = listings.xpath('.//*[@class="Trsdu(0.3s) "]//text()').extract()
            price_change = listings.xpath('.//*[@class="Trsdu(0.3s) Fw(600) C($dataGreen)"]//text()').extract()
            volume = listing.xpath('.//*[@aria-label="Volume"]/span/text()').extract()

            yield {'Symbol': symbols,
                    'Intraday Price': intraday_price,
                    'Price Change': price_change,
                    'Volume': volume}
