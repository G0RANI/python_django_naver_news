from django.shortcuts import render, redirect

from django.views import View
from django.views import generic
from NaverCrawlingDjango import naver_crawler
from django import forms

# Create your views here.
class SearchForm(forms.Form):
    word = forms.CharField(max_length=10, widget=forms.TextInput)

class Crawling_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        form = SearchForm()
        template_name = 'crawling_main/index.html'
        return render(request, template_name, {"form": form})

def result(request):
    template_name = 'crawling_main/result.html'
    word = request.POST['word']
    form = SearchForm()
    object = naver_crawler.fetch_naver_latest_data(word)
    result = object['result']
    title_list = object['title_list']
    naver_crawler.make_wordcloud(title_list)
    return render(request, template_name, {"result": result})