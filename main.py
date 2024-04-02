import os.path
from crawler.vne_crawler import VNECrawler
from utils import ContentWriter
import threading


def extract_newspaper(category, page_number=1, site="vne", limit=None, output_path="data/vne.csv"):
    if site == "vne":
        crawler = VNECrawler()
    else:
        raise ValueError("Site is not supported")

    count = 0
    for page_num in range(1, page_number + 1):
        urls = crawler.get_urls_from_category(category, page_num)
        for url in urls:
            content = crawler.get_information(url)
            content["category"] = category

            ContentWriter.write_csv(output_path, content)

            count += 1
            if limit is not None and count == limit:
                break


if __name__ == "__main__":
    categories = ["the-thao", "giao-duc", "phap-luat", "the-gioi"]
    # category = "the-thao"
    site = "vne"
    threads = []
    # output_path = os.path.join('data')
    for category in categories:
        thr1 = threading.Thread(target=extract_newspaper, args=(category, 20, site, None, "data/vne__" + category + ".csv"))
        thr1.start()
        threads.append(thr1)

    for thr in threads:
        thr.join()
