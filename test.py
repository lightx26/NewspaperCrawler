import os.path

from utils import ContentWriter
from crawler.vne_crawler import VNECrawler

crawler = VNECrawler()

output_path = os.path.join('data', 'vne.csv')

# categories = ['the-gioi', 'the-thao', 'giao-duc', 'phap-luat']
category = 'the-gioi'

for page_num in range(1, 21):
    urls = crawler.get_urls_from_category(category, page_num)
    for url in urls:
        content = crawler.get_information(url)
        content['category'] = category
        ContentWriter.write_csv(output_path, content)