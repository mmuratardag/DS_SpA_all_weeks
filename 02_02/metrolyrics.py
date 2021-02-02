
"""
How to install scrapy:
pip install scrapy OR conda install scrapy

How to run this script:
>>> scrapy runspider -L WARNING metrolyrics.py

To output to a file:
>>> scrapy runspider -L WARNING -o data.csv metrolyrics.py
"""



import scrapy
from scrapy.http import Request
import re

class LyricsSpiderSpider(scrapy.Spider):
    name = 'lyrics_spider'
    allowed_domains = ['www.metrolyrics.com']
    start_urls = ['http://www.metrolyrics.com/top-artists.html/']

    def parse(self, response):

        #this is where we put our Xpath instructions
        artists = response.xpath('//a[@class="image"]/@href').getall()
        for a in artists:
            # print(Request(a))
            yield Request(a)

        songs = response.xpath('//td/a/@href').getall()
        for s in songs:
            yield Request(s)

        text = response.xpath('//div[@id="lyrics-body-text"]//text()').getall()
        #how could you write an Xpath expression to extract the artist name as well?

        text = ' '.join(text)
        text = re.sub('\n|\r|\t', '', text)

        item = {'text': text}
        yield item

        print(text)