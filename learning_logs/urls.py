'''define the URL pattern of learning_logs'''
from django.conf.urls import url

from . import views

urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),

    # show all the topics
    url(r'^topics/$', views.topics, name='topics'),

    # page of a certain topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # add new topic
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # add new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # edit the entry
    url(r'^edit_entry/(?P<entry_id>\d+)$', views.edit_entry, 
        name='edit_entry'),
]