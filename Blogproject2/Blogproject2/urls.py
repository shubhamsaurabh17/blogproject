"""Blogproject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from TestApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include("django.contrib.auth.urls")),
    url(r'^$', views.list_view),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[- \w]+)/$', views.post_view,name='post_detail'),
    url(r'^(?P<id>\d+)/share/$', views.mail_view),
    url(r'^mail/', views.mail_view),
    url(r'^logout/', views.logout_view),
    url(r'^signup/', views.signup_view),
    url(r'^about/', views.about_view),
    url(r'^feedb/', views.feedback_view),
    url(r'^thank/', views.thanks_view),
    url(r'^con/', views.contact_view),
    url(r'^tag/(?P<tag_slug>[- \w]+)/$', views.list_view, name='post_list_by_tag_name'),
]
