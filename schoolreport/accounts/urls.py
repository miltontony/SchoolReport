from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('accounts.views',
    url(r'^profile/$', 'profile_detail', name='accounts_profile'),
    url(r'^profile/(?P<pk>\d+)/$', 'profile_detail', name='accounts_profile'),
)
