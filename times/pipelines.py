# -*- coding: utf-8 -*-

import os
import time

from scrapy.exporters import CsvItemExporter


def _generate_filename(spider, date_format="%Y-%m-%d_%H:%M:%S"):
    _prepare_file_folders(spider)
    time_appendix = time.strftime(date_format)
    return spider.settings.get("FEED_URI_CSV") % ({"name": spider.name, "time": time_appendix})


def _prepare_file_folders(spider):
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/%s' % spider.name):
        os.mkdir('data/%s' % spider.name)


class CsvWriterPipeline(object):

    def open_spider(self, spider):
        filename = _generate_filename(spider)
        self.file = open(filename, 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
