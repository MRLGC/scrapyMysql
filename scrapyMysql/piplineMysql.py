import logging
from twisted.enterprise import adbapi
from scrapyMysql.dbfilter import dbFilter

class PiplineMysql(dbFilter):

    def __init__(self, dbpool, tableInfo, *args):
        self.dbpool = dbpool
        self.tableInfo = tableInfo

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8'
        )
        dbpool = adbapi.ConnectionPool('mysql.connector', **dbparms)
        tableInfo = settings.get('TABLE_ITEM_INFO')
        return cls(dbpool, tableInfo)
    
    def handle_error(self, falure):
        logger = logging.getLogger('PipelineTwisted errors')
        logger.info('{}'.format(falure))
    
    def insert_process(self, cursor, item):
        itemName = item.__class__.__name__
        itemInfo = self.tableInfo.get(itemName, None)
        if itemInfo is not None:
            itemTable = itemInfo.get('table')
            filterColumn = itemInfo.get('filter', [])
            if self.get_rip_data(itemTable, cursor, item, *filterColumn):
                key_line, value_list = self.get_key_value_line(item)
                sql_line = self.make_sql_line(itemTable, key_line, value_list)
                self.excute_sql(sql_line, value_list, cursor)
            else:
                logger = logging.getLogger('{} filter the item'.format(itemName))
                logger.info('the item has stored')
        else:
            raise 'Please check the TABLE_ITEM_INFO in Settings.py'
    

      