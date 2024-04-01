import requests
import sys
from pathlib import Path

from bs4 import BeautifulSoup


class VNECrawler:
    def __init__(self):
        # self.article_type_dict = {
        #     0: 'the-gioi',
        #     1: 'the-thao',
        #     2: 'giao-duc',
        #     3: 'phap-luat',
        #     4: 'suc-khoe',
        #     5: 'du-lich',
        #     6: 'doi-song',
        #     7: 'giai-tri'
        # }
        self.soup = None

    def __set_url(self, url):
        response = requests.get(url).content
        if response is None:
            sys.exit('Error: Could not retrieve the page')
        self.soup = BeautifulSoup(response, 'html.parser')

    def __get_title(self):
        title = self.soup.find('h1', class_='title-detail')

        if title is None:
            return ''

        return title.get_text()

    def __get_date(self):
        date = self.soup.find('span', class_='date')

        if date is None:
            return ''

        return date.get_text()

    def __get_author(self):
        author = self.soup.find('strong')

        if author is None:
            return ''

        return author.get_text()

    def __get_description(self):
        description = self.soup.find('p', class_='description')

        if description is None:
            return ''

        return description.get_text()

    def __get_paragraphs(self):
        paragraphs = self.soup.find_all('p', class_='Normal')
        return [p.get_text() for p in paragraphs]

    def __get_content(self):
        return '\n'.join(self.__get_paragraphs())

    def get_information(self, url):
        self.__set_url(url)
        return {
            'title': self.__get_title(),
            'description': self.__get_description(),
            'content': self.__get_content(),
            'author': self.__get_author(),
            'date': self.__get_date(),
            'url': str(url)
        }

    def get_urls_from_category(self, category, page_number):
        url = f'https://vnexpress.net/{category}'
        if page_number > 1:
            url += f'-p{page_number}'

        self.__set_url(url)

        titles = self.soup.find_all(class_="title-news")
        articles_urls = list()

        for title in titles:
            link = title.find_all("a")[0]
            articles_urls.append(link.get("href"))

        return articles_urls

    # def save(self, path):
    #     with open(path, 'w') as f:
    #         f.write(self.get_title() + '\n')
    #         f.write(self.get_content() + '\n')
    #         f.write(self.get_image() + '\n')
