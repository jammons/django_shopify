from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
    url(r"^starting-an-app/$", direct_to_template, {"template": "help/starting_an_app.html"}, name="starting_an_app"),
    url(r"^editing_shopify_settings/$", direct_to_template, {"template": "help/editing_shopify_settings.html"}, name="editing_shopify_settings"),
)
