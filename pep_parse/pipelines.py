import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from pep_parse.constants import RESULT_DIR, STATUS


BASE_DIR = Path.cwd()


class PepParsePipeline:
    def __init__(self):
        self.res_dir = BASE_DIR / RESULT_DIR
        self.res_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counter[item[STATUS]] += 1
        return item

    def close_spider(self, spider):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        with open(
            f'{self.res_dir}/status_summary_{timestamp}.csv',
             'w',
             newline='',
             encoding='utf-8'
             ) as file:
            writer = csv.writer(file)
            writer.writerows(
                (('Статус', 'Количество'),
                 *self.status_counter.items(),
                 ['Total:', sum(self.status_counter.values())])
            )
