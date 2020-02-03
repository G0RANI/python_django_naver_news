import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

def fetch_naver_latest_data():
    result = []

    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    web_page_link_root = "https://search.naver.com"
    list_items = soup.find_all("a", "_sp_each_title")

    for item in list_items:
        # title
        title = item.text

        # link
        link = item["href"]
        page_link_raw = web_page_link_root + item["href"]
        page_link_parts = urlparse(page_link_raw)
        normalized_page_link = page_link_parts.scheme + '://' + page_link_parts.hostname + page_link_parts.path

        # specific id
        specific_id = page_link_parts.path.split('/')[-1]

        item_obj = {
            'title': title,
            'link': normalized_page_link,
            'specific_id': specific_id,
        }

        print(title)
        result.append(item_obj)

    return result




