import csv
from datetime import datetime
from pathlib import Path

from pep_parse.constants import RESULT_DIR, STATUS


BASE_DIR = Path.cwd()


class PepParsePipeline:
    def __init__(self):
        self.status_counter = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.status_counter[item[STATUS]] = (
            self.status_counter.get(item[STATUS], 0) + 1)
        return item

    def close_spider(self, spider):
        res_dir = BASE_DIR / RESULT_DIR
        res_dir.mkdir(exist_ok=True)
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        with open(
            f'{res_dir}/status_summary_{timestamp}.csv',
             'w',
             newline='',
             encoding='utf-8'
             ) as file:
            writer = csv.writer(file)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_counter.items())
            writer.writerow(['Total:', sum(self.status_counter.values())])
