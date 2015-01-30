from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('product.views',
	url(r'^$', 'view_all', name='view_all'),
	url(r'category/(?P<category>[-\w]+)$', 'view_by_category', name='product_in_category'),
	url(r'product/(?P<slug>[-\w]+)$', 'product', name='product'),
)
