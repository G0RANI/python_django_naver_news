from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'crawling_main'

urlpatterns = [
    url(r'^$', views.Crawling_main.as_view(), name='crawling_main'),
    url('result', views.result, name='result'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)