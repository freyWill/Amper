
from django.shortcuts import render, render_to_response
from .models import Product, Category
from django.http import HttpResponse
from Amper.views import baseDict, cartItems
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404
from itertools import chain
from django.core.context_processors import csrf
from cart import Cart

def products_paginated(request, products): # a shortcut function for quick pagination

	paginator = Paginator(products,10)
	page = request.GET.get('page')

	try:
		paginated_products = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		paginated_products = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		paginated_products = paginator.page(paginator.num_pages)

	return paginated_products

def product(request,slug):
	product = get_object_or_404(Product, slug=str(slug))
	dictionary = baseDict(request) # fetch the common data
	cartItems(request, dictionary) # get the cart items in a form of a dictionary, so that templates can display if item has been added or not
	productCategory = Category.objects.get(slug=product.category.slug)

	dictionary.update({
		'product' : product,
		'nodes' : Category.objects.get(slug=product.category.slug,),
		'page_title' : str(product.title) + " - Amper",
	})

	return render_to_response("single_product.html", dictionary, context_instance = RequestContext(request))

def view_all(request):

	c = {}
	c.update(csrf(request)) # token is required, because there is an add to cart form

	products = Product.objects.all()

	dictionary = baseDict(request)
	cartItems(request, dictionary)

	dictionary.update({
		'products' : products_paginated(request, products),
		'page_title' : 'Products - Amper',
		'nodes' : Category.objects.all(),
	})

	return render_to_response("products.html", dictionary, context_instance = RequestContext(request))

def view_by_category(request, category="-111"):

	dictionary = baseDict(request)

	children = Product.objects.filter(category__parent__slug=category) # so that all subcategory products can be fetched and displayed
	direct = Product.objects.filter(category__slug=category)					 # fetches the current product branch
	products = list(chain(children, direct))                           # this line joins them

	cartItems(request, dictionary) 

	dictionary.update({
		'products' : products_paginated(request, products),
		'nodes' : Category.objects.all(),
	})

	return render_to_response("products.html", dictionary, context_instance = RequestContext(request))
