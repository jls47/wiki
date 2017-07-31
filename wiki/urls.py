"""wiki URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import include


from articles.views import about, get_all_articles, get_one_article, get_write_page, get_featured_articles, get_edit_page, get_talk_page
from profiles.views import about, get_one_profile, get_all_profiles, about

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'frontpage.html'}, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^articles/featured/', get_featured_articles),
    url(r'^articles/talk/(?P<pk>\d+)/', get_talk_page),
    url(r'^articles/edit/(?P<pk>\d+)/', get_edit_page),
    url(r'^articles/write/', get_write_page),
    url(r'^articles/(?P<pk>\d+)/', get_one_article),
    url(r'^profiles/all/', get_all_profiles),
    url(r'^profiles/about/', get_one_profile),
    url(r'^profiles/(?P<pk>\d+)/', get_one_profile),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^articles/all', get_all_articles),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', admin.site.urls),
]
