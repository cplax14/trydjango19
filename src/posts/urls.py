from django.conf.urls import url
from django.contrib import admin

#this is apparently deprecated in Django 1.10
#from . import views

from .views import (
	posts_list,
	posts_create,
	posts_detail,
	posts_update,
	posts_delete)

#from posts import views as postsviews

urlpatterns = [
    
    #url(r'^posts/$', postsviews.posts_home, name='PostsHome'),
    #url(r'^home$', "posts.views.posts_home"),
    
    #commenting out the string based view invocation
    # url(r'^$', "posts.views.posts_list"),    
    # url(r'^create$', "posts.views.posts_create"),
    # url(r'^detail$', "posts.views.posts_detail"),
    # #url(r'^list$', "posts.views.posts_list"),

    # url(r'^update$', "posts.views.posts_update"),
    # url(r'^delete$', "posts.views.posts_delete"),

#     url(r'^$', posts_list, name='list'),    
#     url(r'^create/$', posts_create),
# #    url(r'^detail$', posts_detail),
# 	#url(r'^detail/(?P<id>\d+)/$', posts_detail),
# 	url(r'^(?P<id>\d+)/$', posts_detail, name='detail'),
#     #url(r'^list$', "posts.views.posts_list"),

#     url(r'^(?P<id>\d+)/edit/$', posts_update, name='update'),
#     url(r'^(?P<id>\d+)/delete/$', posts_delete),
    url(r'^$', posts_list, name='list'),
    url(r'^create/$', posts_create),
    url(r'^(?P<slug>[\w-]+)/$', posts_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', posts_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', posts_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),


]