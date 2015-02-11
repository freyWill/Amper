from django.db import models
import random
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User
import string

class Order(models.Model):
	orderId = models.CharField(max_length=30, blank=True)
	user = models.ForeignKey(User)
	items  = models.ManyToManyField(Product, blank=True)
	itemQuantityList = models.CharField(max_length=4000)
	itemPriceList = models.CharField(max_length=4000)
	totalAmount = models.FloatField(default=0)
	completed = models.BooleanField(default=False)
	orderDate = models.DateTimeField(default=timezone.now)
	completedDate = models.DateTimeField(blank=True, null=True)


	# def __str__(self):
	# 	return self.orderDate

@receiver(pre_save, sender=Order)
def generateId(sender, instance, **kwargs):
	randomId = ""
	for i in range(0,10):
		randomId += random.choice(string.letters).title()
	instance.orderId = randomId