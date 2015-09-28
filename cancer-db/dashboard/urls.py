from django.conf.urls import url
from . import views


try:
    from django.conf.urls import patterns, url, include
except:
    from django.conf.urls.defaults import patterns, url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    	url(r'^$', views.index, name='index'),
    	url(r'^db/(?P<db_name>\w+)/$', views.db_search, name='db_search'),
    	url(r'^db/(?P<db_name>\w+)/download$', views.db_download, name='db_download'),
    	url(r'^search/$', views.general_search, name='general_search'),
    	url(r'^get/(?P<DB_ID>\w+)/$', views.detail, name='detail'),
    	url(r'^mark/(?P<DB_ID>\w+)/$', views.mark, name='mark'),
    	url(r'^confirm/$', views.confirm, name='confirm'),

    	url(r'^db/(?P<DB_ID>\w+)/(?P<mode>\w+)/$', views.db_add_edit,{}, name='addentry'),
		url(r'^db/(?P<DB_ID>\w+)/(?P<mode>\w+)/(?P<object_id>\w+)/$', views.db_add_edit,{}, name='editentry'),
		url(r'^db/(?P<DB_ID>\w+)/(?P<mode>\w+)/(?P<object_id>\w+)/(?P<instance_id>\w+)/$', views.db_add_edit,{}, name='editentry'),


]
