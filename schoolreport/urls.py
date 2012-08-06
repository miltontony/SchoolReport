from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'schoolreport.views.home', name='home'),
    url(r'^$', 'schoolreport.views.home', name='index'),
    url(r'^page/(?P<page>\d+)/$', 'schoolreport.views.home', name='home'),
    url(r'^join/$', 'schoolreport.auth.join', name='join'),
    url(r'^login/$', 'schoolreport.auth.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^schoolreport/comments/', include('jmbocomments.urls')),

    url(r'^health/', 'schoolreport.views.health', name='health'),
    url(r'^cgi-sys/defaultwebpage.cgi$', redirect_to, {'url': '/'}),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),
    )
