import csv
from datetime import datetime


class PepParsePipeline:
    def __init__(self):
        self.status_counter = {}

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.status_counter[item['status']] = (
            self.status_counter.get(item['status'], 0) + 1)
        return item

    def close_spider(self, spider):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        with open(
            f'results/status_summary_{timestamp}.csv',
             'w',
             newline='',
             encoding='utf-8'
             ) as file:
            writer = csv.writer(file)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_counter.items())
            writer.writerow(['Total:', sum(self.status_counter.values())])
