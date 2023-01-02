import scrapy

# -*- coding: utf-8 -*-
import scrapy

# The simplest possible scrapy program.


class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ["http://books.toscrape.com"]

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'title': article.css("h3 > a::attr(title)").get(),
                'stars': article.css("p::attr(class)").get().split(" ")[-1],
                'price': article.css("p.price_color::text").get(),
                'stock': article.css("p.instock.availability::text").getall()[1].split(" ")[12]
            }

        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)