import os.path
from crawler.vne_crawler import VNECrawler
from utils import ContentWriter


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
    category = "the-thao"
    site = "vne"
    output_path = os.path.join('data', site + "_" + category + '.csv')
    extract_newspaper(category, 20, site=site, output_path=output_path)
