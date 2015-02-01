
from django.shortcuts import render, render_to_response
from .models import Product, Category
from django.http import HttpResponse
from Amper.views import baseDict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404
from itertools import chain
from django.core.context_processors import csrf

def product(request,slug):
	product = get_object_or_404(Product, slug=str(slug))
	dictionary = baseDict(request)

	productCategory = Category.objects.get(slug=product.category.slug)

	dictionary.update({
		'product' : product,
		'nodes' : Category.objects.get(slug=product.category.slug,),
		'page_title' : str(product.title) + " - Amper",
	})

	return render_to_response("single_product.html", dictionary, context_instance = RequestContext(request))

def view_all(request):
	c = {}
	c.update(csrf(request))
	
	products = get_list_or_404(Product)
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

	dictionary = baseDict(request)
	dictionary.update({
		'products' : paginated_products,
		'page_title' : 'Products - Amper',
		'nodes' : Category.objects.all(),
		'token' : c,
	})

	return render_to_response("all_products.html", dictionary, context_instance = RequestContext(request))

def view_by_category(request, category="-111"):
	dictionary = baseDict(request)

	children = Product.objects.filter(category__parent__slug=category)	
	direct = get_list_or_404(Product.objects.filter(category__slug=category))
	products = list(chain(children, direct))

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

	dictionary.update({
		'products' : paginated_products,
		'nodes' : Category.objects.all(),
	})

	return render_to_response("all_products.html", dictionary, context_instance = RequestContext(request))

