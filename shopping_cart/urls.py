from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('shopping_cart.views',
	url(r'^$', 'view_cart', name='view_cart'),
	# url(r'add/(?P<product_slug>[-\w]+)/(?P<quantity>\d+)$', 'add_to_cart', name='add_to_cart'),
	url(r'remove/(?P<product_slug>[-\w]+)$', 'remove_from_cart', name='remove_item_from_cart'),
	url(r'add_by_post$', 'add_to_cart_via_post', name='add_by_post'),

)
