
"""
How to install scrapy:
pip install scrapy OR conda install scrapy

How to run this script:
>>> scrapy runspider -L WARNING allthelyrics.py

To output to a file:
>>> scrapy runspider -L WARNING -o rolling_stones.csv allthelyrics.py
"""

import scrapy
from scrapy.http import Request
import re


class SongSpider(scrapy.Spider):
    name = "Dead K Scraper"
    allowed_domains = ["www.allthelyrics.com"]
    start_urls = ["https://www.allthelyrics.com/de/lyrics/dead_kennedys"]
    custom_settings = {
        'DEPTH_LIMIT': 10,
        'AUTOTHROTTLE_ENABLED': False,
        #see: https://docs.scrapy.org/en/latest/topics/autothrottle.html#autothrottle-extension

    }

    def parse(self, response):
        songlinks = response.xpath(
            "//li[contains(@class, 'lyrics-list-item')]/a/@href"
        ).getall()

        for sl in songlinks:
            yield Request(response.urljoin(sl))

        song_text = response.xpath(
            "//div[contains(@class, 'content-text')]//p//text()"
        ).getall()

        clean_text = "".join(song_text)
        clean_text = re.sub("\n", " ", clean_text)

        item = {"lyrics": clean_text, "artist": "dead kennedys"}
        print(item)
        yield item
