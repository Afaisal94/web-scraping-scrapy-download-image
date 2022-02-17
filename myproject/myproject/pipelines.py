from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class MyprojectPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'book_name': item.get('book_name')}) for x in item.get(self.images_urls_field, [])]

    def file_path(self, request, response=None, info=None, *, item=None):
        filename = request.meta['book_name'].replace(':', '').replace(',', '')
        return 'full/%s.jpg' % (filename)
