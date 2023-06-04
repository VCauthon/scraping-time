# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

import sys
sys.path.append('/..')
from db.crud import CRUD  # noqa: E402


class FotocasaPipeline:
    def process_item(self, item, spider):

        # Insert the item in the DB
        CRUD.insert('fotocasa_tb', item)
        return item
