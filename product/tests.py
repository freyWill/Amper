from django.test import TestCase, RequestFactory
from product.views import products_paginated
# Create your tests here.
class ProductTestClass(TestCase):
	def test_generic(self):
		self.assertEquals("h","h")