import scrapy

from pep_parse.constants import NAME, NUMBER, STATUS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        rows = response.css('tr')
        for row in rows:
            pep_link = row.css('a.pep.reference.internal::attr(href)').get()
            if pep_link:
                yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get()
        number, name = pep_title.split(' – ', maxsplit=1)
        data = {
            NUMBER: int(number.split()[1]),
            NAME: name,
            STATUS: response.css('abbr::text').get()
        }
        yield PepParseItem(data)
