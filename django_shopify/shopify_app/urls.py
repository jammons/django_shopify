from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('{{ project_name }}.shopify_app',
        url(r'^$', 'views.login', name='shopify_login'),
        url(r'^authenticate/$', 'views.authenticate', name='shopify_auth'),
        url(r'^finalize/$', 'views.finalize', name='shopify_finalize'),
        url(r'^logout/$', 'views.logout', name='shopify_logout'),
)
