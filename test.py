import os.path

from utils import ContentWriter
from crawler.vne_crawler import VNECrawler

crawler = VNECrawler()

output_path = os.path.join('data', 'test.csv')

# categories = ['the-gioi', 'the-thao', 'giao-duc', 'phap-luat']
# category = 'the-gioi'

# for page_num in range(1, 21):
#     urls = crawler.get_urls_from_category(category, page_num)
#     for url in urls:
#         content = crawler.get_information(url)
#         content['category'] = category
#         ContentWriter.write_csv(output_path, content)

# crawler.__set_url('https://vnexpress.net/10-doi-giay-chay-tot-cho-cac-bai-tap-toc-do-4727692.html')
# print(crawler.__get_title())
# print(crawler.__get_description())
print(crawler.get_information("https://vnexpress.net/hlv-park-hang-seo-du-dam-cuoi-quang-hai-4727681.html"))