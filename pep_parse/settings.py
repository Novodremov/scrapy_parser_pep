from pep_parse.constants import BOT_NAME, NAME, NUMBER, RESULT_DIR, STATUS


SPIDER_MODULES = [f'{BOT_NAME}.spiders']
NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    f'{BOT_NAME}.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'{RESULT_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': [NUMBER, NAME, STATUS],
        'overwrite': True
    },
}
