from django.shortcuts import render_to_response
from user_profile.models import UserProfile
from controller.models import Slide
from product.models import Product
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404
from cart import Cart

def home(request):

	dictionary = baseDict(request)
	dictionary.update({

		"slides" : get_list_or_404(Slide, display=True) ,
		"top_products" : get_list_or_404(Product.objects.order_by("purchased")[:4]),
	})

	return render_to_response("index.html", dictionary, context_instance = RequestContext(request))


def baseDict(request):
	item_count = 0
	for i in Cart(request):
		item_count+=1

	user = request.user
	dictionary = {
		'user' : user,
		'cart_item_count' : item_count,
	}

	if request.user.is_authenticated():
		
		dictionary.update({
			'userProfile' : UserProfile.objects.get(user=user),
		
		})

	return dictionary