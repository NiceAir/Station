# -*- coding:utf-8 -*-
#  made in ly


from django.db.models.aggregates import Count
from ..models import Post, Category, Tag
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_in_time():
    return Post.objects.dates('created_time', 'month', order='DESC')    #DESC 降序

@register.simple_tag
def get_categories():
  #  return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return Category.objects.all()

@register.simple_tag()
def get_tag_cloud():
    return Tag.objects.all()

@register.simple_tag()
def get_popular_post(num=9):
    return Post.objects.all().order_by('-views')[:num]


'''
@register.simple_tag()
def get_author():
    return Post.objects.all()
'''