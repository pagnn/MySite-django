from django.conf.urls import url,include
from .views import blog_title,blog_content


urlpatterns = [
    url(r'^$', blog_title,name='blog_title'),
    url(r'(?P<article_id>\d)/$', blog_content,name='blog_title'),
]
