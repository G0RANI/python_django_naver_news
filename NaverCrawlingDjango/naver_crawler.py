import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

from konlpy.tag import Twitter
from collections import Counter
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator

import numpy as np
from PIL import Image


def fetch_naver_latest_data(word):
    result = []
    title_list = []
    page = 1
    maxpage_t = (int(5) - 1) * 10 + 1

    while page <= maxpage_t:
        url = 'https://search.naver.com/search.naver?&where=news&query='+word+'&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=75&start='+ str(page) +'&refresh_start=0'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        list_items = soup.find_all("a", "_sp_each_title")

        web_page_link_root = "https://search.naver.com"
        for item in list_items:

            title = item.text

            link = item["href"]
            page_link_raw = web_page_link_root + item["href"]
            page_link_parts = urlparse(page_link_raw)

            item_obj = {
                'title': title,
                'link': link,
            }
            title_list.append(title)
            result.append(item_obj)
        page += 10
    return {
        'result': result,
        'title_list': title_list,
    }

def make_wordcloud(title_list):
    twitter = Twitter()

    sentences_tag = []

    for sentence in title_list:
        morph = twitter.pos(sentence)
        sentences_tag.append(morph)

    noun_adj_list = []

    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective']:
                noun_adj_list.append(word)

    counts = Counter(noun_adj_list)
    tags = counts.most_common(2000)

    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    mask = np.array(Image.open(os.path.join(d+'/crawling_main/static/img/mask/kor_mask.png')))
    data = dict(tags)
    wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',  background_color = 'white', mask = mask).generate(' '.join(data))
    image_colors = ImageColorGenerator(mask)
    plt.figure(figsize=(10, 8))
    plt.imshow(wc.recolor(color_func = image_colors), interpolation='bilinear')
    plt.axis('off')
    plt.savefig(os.path.join(d+"/crawling_main/static/img", "wordcloud.png"))
