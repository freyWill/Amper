from django.shortcuts import render,render_to_response,redirect, HttpResponseRedirect
from cart import Cart
from product.models import Product
from Amper.views import baseDict
from django.template import RequestContext
from controller.models import Slide
from django.shortcuts import get_list_or_404, get_object_or_404

def update_dict_for_main_page_redirect(dictionary):
	dictionary.update({
		"slides" : get_list_or_404(Slide, display=True) ,
		"top_products" : get_list_or_404(Product.objects.order_by("purchased")[:4]),
	})

# def add_to_cart(request, product_slug, quantity):
# 	dictionary = baseDict()
# 	update_dict_for_main_page_redirect(dictionary)

# 	if quantity <= 0:
# 		print "error detected"
# 		dictionary.update({
# 			"quantity_error" : "The quantity you added is less than zero, please put a positive number !"
# 		})
# 		return redirect('Amper.views.home', dictionary, context_instance = RequestContext(request))


# 	product = Product.objects.get(slug=product_slug)
# 	cart = Cart(request)
# 	cart.add(product, product.price, quantity)
# 	return redirect('Amper.views.home', dictionary, context_instance = RequestContext(request))

def remove_from_cart(request, product_slug):
	dictionary = baseDict(request)
	update_dict_for_main_page_redirect(dictionary)

	product = Product.objects.get(slug=product_slug)
	cart = Cart(request)
	cart.remove(product)

	return render_to_response('cart.html', dictionary, context_instance = RequestContext(request))

def view_cart(request):
	dictionary = baseDict(request)
	dictionary.update({
		'cart' : Cart(request)
	})

	return render_to_response('cart.html', dictionary, context_instance = RequestContext(request))

def add_to_cart_via_post(request):
	dictionary = baseDict(request)
	update_dict_for_main_page_redirect(dictionary)
	
	quantity = request.POST.get('quantity')

	if int(quantity) <= 0:
		print "error detected"
		dictionary.update({
			"error_message" : "The quantity you added is %s, please put a positive number !" % quantity
		})
		# return render_to_response('index.html', dictionary, context_instance = RequestContext(request))
		return render_to_response("index.html", dictionary, context_instance = RequestContext(request))

	product_slug = request.POST.get('slug')
	product = Product.objects.get(slug=product_slug)

	cart = Cart(request)
	cart.add(product, product.price, quantity)


	# return render_to_response('index.html', dictionary, context_instance = RequestContext(request))
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))