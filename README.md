# scrapyMysql<br>
make scrapy crawled data store into mysql easier.

How to use
-
`pip install scrapyMysql`<br>
you must first add the new configuration to the your setting file:<br>
```
TABLE_ITEM_INFO = {
    'itemclassname':{
    table:'tableneme',
    filter:['column']
    },
    'itemclassname':{
    table:'tableneme',
    filter:['column']
    },
}
```
param:<br>
* `itemclassname`:str, item object class name that you defined in the scrapy item file
* `tablename`:str, the name of the table which item stored
* `filter`:list,this is option, you can use the table column name as the filter condition

then you can use this package in your pipeline file:<br>
```
from scrapyMysql import PiplineMysql

class ScrapysqlitemPipeline(PiplineMysql):
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.insert_process, item)
        query.addErrback(self.handle_error)
        return item
```
now you can foce on write your scrapy spiders
