"""cancer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'cancer.views.login_view'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^dashboard/',include('dashboard.urls')),

	#login logout
	url(r'^accounts/login/$',  'cancer.views.login_view'),
    url(r'^accounts/logout/$', 'cancer.views.logout_view'),
    url(r'^accounts/loggedin/$', 'cancer.views.loggedin'),
   	url(r'^accounts/register/$', 'cancer.views.register_user'),
    url(r'^accounts/register_success/$', 'cancer.views.register_success'),
	url(r'^accounts/logout_success/$', 'cancer.views.logout_success'),

    url(r'session_security/', include('session_security.urls')),

	url(r'^help/$',  'cancer.views.help'),	
]
