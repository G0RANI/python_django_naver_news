import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

def fetch_naver_latest_data():
    result = []

    page = 1
    maxpage_t = (int(10) - 1) * 10 + 1

    while page <= maxpage_t:
        url = 'https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=75&start='+ str(page) +'&refresh_start=0'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        list_items = soup.find_all("a", "_sp_each_title")

        web_page_link_root = "https://search.naver.com"
        for item in list_items:
            # title
            title = item.text

            # link
            link = item["href"]
            page_link_raw = web_page_link_root + item["href"]
            page_link_parts = urlparse(page_link_raw)

            item_obj = {
                'title': title,
                'link': link,
            }

            result.append(item_obj)
        page += 10

    return result
