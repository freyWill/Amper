from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from .views import baseDict, cartItems, fetchMostPurchasedProducts
from product.views import Product, Category
from autofixture import AutoFixture
from cart import Cart

class BaseTest(TestCase):

	def setUp(self):
		self.factory = RequestFactory()
		self.user = User.objects.create_user(username='john', email='john@email.com', password='top_secret')
		
	def test_basedict_returnsdatain_index_with_empty_cart(self):
		
		request = self.factory.get("http://localhost:8000")
		request.user = self.user
		request.session = {}

		dictionary = baseDict(request)

		self.assertEquals("Amper", dictionary['page_title'])
		self.assertEquals('john', dictionary['user'].username)
		self.assertEquals(0, dictionary['cart_item_count'])

	def generateCartWithItems(self, request):
		fixture = AutoFixture(Category)
		category = fixture.create(1)

		fixture = AutoFixture(Product)
		products = fixture.create(5) # 5 products
		quantity = 3 # added 3 times, thus 5*3=15
		products[0].title="kartofi"
		products[1].title="makaroni"
		cart = Cart(request)
		for product in products:
			cart.add(product, product.price, quantity)
		return cart

	def test_basedict_returnsdatain_index_with_nonempty_cart(self):
		request = self.factory.get("http://localhost:8000")
		request.user = self.user
		request.session = {}

		cart = self.generateCartWithItems(request)
		
		dictionary = baseDict(request)
		self.assertEquals(15, dictionary['cart_item_count'])

	def test_cart_items_access_is_possible(self):

		dictionary = {}
		request = self.factory.get("/")
		request.session = {}
		request.user = self.user
		cart = self.generateCartWithItems(request)
		cartItems(request, dictionary)

		self.assertTrue(3, dictionary['cart'])

	def canGetMostPurchasedProducts(self):
		fixture = AutoFixture(Product)
		products = fixture.create(10)
		counter = 10
		for product in products:
			product.purchased = counter-1
			product.save()

		popularProducts = fetchMostPurchasedProducts(4)

		for i in range(0,len(popularProducts)):
			self.assertEquals(popularProducts[i], products[ic])
