import json

import scrapy

from ipanda.items import IpandaItem
from string import Template

class PandaSpider(scrapy.Spider):
    name = 'panda'
    #allowed_domains = ['news.ipanda.com','api.cntv.cn','img.cctvpic.com']
    start_urls = []

    def __init__(self,  *args, **kwargs):
        super(PandaSpider, self).__init__(*args, **kwargs)

        page_list = range(1,20)
        url_template = Template( 'https://api.cntv.cn/list/getPhoaListByPageIdAction?id=PAGE1430733736264596&serviceId=panda&p=$page&n=100')
        self.start_urls = [ url_template.substitute(page=str(page)) for page in page_list]

    def parse(self, response):
        resp_json = json.loads(response.body)
        for v in resp_json["data"]:
            imageItem = IpandaItem()
            imageItem["image_urls"]= v["photo_album_logo"]
            imageItem["alt"] = v["photo_album_id"]
            yield  imageItem
