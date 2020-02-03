import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

def fetch_naver_latest_data():
    result = []

    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%9A%B0%ED%95%9C'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    web_page_link_root = "https://search.naver.com"
    list_items = soup.find_all("li")
    print(list_items)
    for item in list_items:
        # title
        title = item.find("a", "_sp_each_title")
        print(title)

        # link
        page_link_raw = web_page_link_root + item.find("href")
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

if __name__ == '__main__':
    fetch_naver_latest_data()




