from django.shortcuts import render,render_to_response,redirect, HttpResponseRedirect
from cart import Cart
from product.models import Product, Category
from Amper.views import baseDict
from django.template import RequestContext
from controller.models import Slide
from django.shortcuts import get_list_or_404, get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse
from shopping_cart.models import Order

def update_dict_for_main_page_redirect(dictionary, request): # this exists, because the cart actions do redirection, and without proper context, the page will look void
	dictionary.update({
		"slides" : get_list_or_404(Slide, display=True) ,
		'cart' : Cart(request),
		'page_title' : 'My cart - Amper',

	})

def remove_from_cart(request, product_slug):
	dictionary = baseDict(request)
	update_dict_for_main_page_redirect(dictionary, request)

	product = Product.objects.get(slug=product_slug) # fetch the product we want to remove
	cart = Cart(request) # fetch the cart
	cart.remove(product) # remove the item

	return render_to_response('cart.html', dictionary, context_instance = RequestContext(request))

def view_cart(request):
	dictionary = baseDict(request)
	update_dict_for_main_page_redirect(dictionary, request)

	totalPrice = 0 # the loop calculates the total price of the shopping cart
	for i in Cart(request):
		totalPrice += i.product.price
	dictionary.update({
		'totalPrice' : totalPrice,
	})


	return render_to_response('cart.html', dictionary, context_instance = RequestContext(request))

def add_to_cart_via_post(request):
	dictionary = baseDict(request)
	update_dict_for_main_page_redirect(dictionary, request)

	quantity = request.POST.get('quantity')

	if int(quantity) <= 0: # stop if the amount added is not positive
		dictionary.update({
			"error_message" : "The quantity you added is %s, please put a positive number !" % quantity,
			'nodes' : Category.objects.all(),
		})
		# return render_to_response('index.html', dictionary, context_instance = RequestContext(request))
		return render_to_response("products.html", dictionary, context_instance = RequestContext(request))

	# otherwise fetch the product and add it's amount to the cart
	product_slug = request.POST.get('slug')
	product = Product.objects.get(slug=product_slug)
	if (int(product.quantity) - int(quantity)) < 0:
		dictionary.update({
			'error_message' : '%s has %d items left in stock !' % (product.title, product.quantity),
			'nodes' : Category.objects.all(),
		})
		return render_to_response("products.html", dictionary, context_instance = RequestContext(request))

	cart = Cart(request)
	cart.add(product, product.price, quantity)


	# return render_to_response('index.html', dictionary, context_instance = RequestContext(request))
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def checkout(request):
	priceList = []
	quantityList = []
	totalPrice = 0
	order = Order()
	order.user = request.user
	order.save()
	for item in Cart(request):
		totalPrice += item.product.price
		priceList.append(item.product.price)
		quantityList.append(item.product.quantity)
		order.items.add(item.product)
	order.itemQuantityList = priceList
	order.itemPriceList = quantityList
	order.totalAmount = totalPrice
	order.save()

	return render_to_response('index.html')

