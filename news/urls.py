
# -*- coding:utf-8 -*-
#  made in ly

from django.conf.urls import url
from . import views

app_name='news'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
  #  url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name="category"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name="category"),
    url(r'^category_more_post/(?P<pk>[0-9]+)/$', views.category_more_post, name="category_more_post"),
    url(r'hot_topic/$', views.hot_topic, name='hot_topic'),
]