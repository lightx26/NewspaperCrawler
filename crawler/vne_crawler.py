import requests
import sys
from pathlib import Path

from bs4 import BeautifulSoup


class VNECrawler:
    def __init__(self):
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
        article = self.soup.find('article', class_="fck_detail")

        if article is None:
            return '', ''

        author_tag = article.find('p', class_="author_mail")

        # if the article is not use "author_mail", get the last <p Normal> tag
        if author_tag is None:
            pt = article.find_all('p', class_="Normal")
            if len(pt) == 0:
                return '', ''
            author_tag = pt[-1]

        # if the last <p Normal> tag is empty, return empty string - no author
        author = '' if author_tag.find('strong') is None else author_tag.find('strong').get_text()
        ref = '' if author_tag.find('em') is None else author_tag.find('em').get_text()
        return author, ref

    def __get_description(self):
        description = self.soup.find('p', class_='description')

        if description is None:
            return ''

        location = description.find('span', class_="location-stamp")

        if location is None:
            return description.get_text()

        return description.get_text().replace(location.get_text(), '', 1)

    def __get_paragraphs(self):
        article = self.soup.find('article', class_="fck_detail")
        if article is None:
            return []

        paragraphs = article.find_all('p', class_='Normal')

        if len(paragraphs) == 0:
            return []

        return [p.get_text() for p in paragraphs[:-1]]

    def __get_content(self):
        return '\n'.join(self.__get_paragraphs())

    def get_information(self, url):
        self.__set_url(url)
        return {
            'title': self.__get_title(),
            'description': self.__get_description(),
            'content': self.__get_content(),
            'author': self.__get_author()[0],
            'author_ref': self.__get_author()[1],
            'date': self.__get_date(),
            'url': url
        }

    def get_urls_from_category(self, category, page_number):
        url = f'https://vnexpress.net/{category}'
        if page_number > 1:
            url += f'-p{page_number}'

        self.__set_url(url)

        titles = self.soup.find_all(class_="title-news")
        if titles is None:
            return []

        articles_urls = []
        for title in titles:
            link = title.find_all("a")[0]
            if "video.vnexpress.net" in link.get("href"):
                continue
            articles_urls.append(link.get("href"))

        return articles_urls
