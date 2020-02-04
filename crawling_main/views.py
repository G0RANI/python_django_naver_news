from django.shortcuts import render, redirect

from django.views import View
from django.views import generic
from NaverCrawlingDjango import naver_crawler

# Create your views here.
class Crawling_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'crawling_main/index.html'
        result = naver_crawler.fetch_naver_latest_data()
        print(result)
        return render(request, template_name, {"result": result})
