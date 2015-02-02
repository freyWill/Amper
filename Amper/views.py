from django.shortcuts import render_to_response
from user_profile.models import UserProfile
from controller.models import Slide
from product.models import Product
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404
from cart import Cart

def fetchMostPurchasedProducts(number):
	return Product.objects.filter(active=True).order_by("purchased")[:number]

def home(request): # efectivly used as the index page

	dictionary = baseDict(request) # these two methods are defined below
	cartItems(request, dictionary) 
	dictionary.update({
		"slides" : Slide.objects.filter(display=True) ,
		"products" : fetchMostPurchasedProducts(4),
	})

	return render_to_response("index.html", dictionary, context_instance = RequestContext(request)) # context is included so that media url is available

def cartItems(request, dictionary): # The function takes reuqest and the dictionary that the result will be put in
	
	inCartDict = {}
	for item in Cart(request):  # iterate trough the cart
		inCartDict.update({ 			# the key will be the name of a product, and the value is the shopping cart quantity
 			item.product.title : item.quantity, # this is useful when wondering which item has been added and how many times
		})
	
	dictionary.update({ 				# now give that data to the main dictionary
		'cart' : inCartDict,
	})

def baseDict(request):
	item_count = 0
	for i in Cart(request):
		item_count+=i.quantity # counts items in shopping cart

	user = request.user # fetch the current logged in user
	dictionary = {
		'user' : user,
		'cart_item_count' : item_count,
		'page_title' : "Amper"
	}

	if request.user.is_authenticated():

		dictionary.update({
			'userProfile' : UserProfile.objects.get(user=user),

		})

	return dictionary
