BOT_NAME = 'dilerbank'
SPIDER_MODULES = ['dilerbank.spiders']
NEWSPIDER_MODULE = 'dilerbank.spiders'
LOG_LEVEL = 'WARNING'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
   'dilerbank.pipelines.DatabasePipeline': 300,
}
