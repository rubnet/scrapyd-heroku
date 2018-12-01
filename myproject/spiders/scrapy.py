import scrapy
import os
import base64


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    env = os.environ
    
    def getEnv(self, var):
      binVar = env[var].encode('ascii') if env.get(var) else b''
      return base64.b64decode(binVar).decode('ascii')
      
    def start_requests(self):
        domain = getEnv('DOMAIN')
        ip = getEnv('IP')
        user = getEnv('USER')
        passwd = getEnv('PASSWD')
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

