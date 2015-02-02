from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('shopping_cart.views',
	url(r'^$', 'view_cart', name='view_cart'), # displays the cart
	url(r'^remove/(?P<product_slug>[-\w]+)$', 'remove_from_cart', name='remove_item_from_cart'), # removes an item completely from the cart
	url(r'^add_by_post$', 'add_to_cart_via_post', name='add_by_post'), # adds an item to the cart using the add to cart form in the view
	url(r'payment$', 'payment_view', name='make_payment'), # adds an item to the cart using the add to cart form in the view

)
