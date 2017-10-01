import re

from anaconda_project.plugins.network_util import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):

        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    @staticmethod
    def _get_new_urls(page_url, soup):
        new_urls = set()

        # <a target="_blank" href="/item/%E5%8A%A8%E6%80%81%E8%AF%AD%E8%A8%80">动态语言</a>
        links = soup.find_all('a', href=re.compile(r"/item/\w"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        res_data = {'url': page_url}
        # url
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data
