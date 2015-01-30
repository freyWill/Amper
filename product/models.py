from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.utils.safestring import mark_safe
from user_profile.models import UserProfile
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from djangoratings.fields import RatingField
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=250, unique=True, help_text='Specify the url to your product.', null=True, blank=True)
	parent = TreeForeignKey('self', blank=True, null=True, related_name='children')

	def __str__(self):
		return self.title

class Product(models.Model):

	title = models.CharField(max_length=300, unique=True, help_text='Give the name of the product.', null=False, blank=False)
	slug = models.SlugField(max_length=250, unique=True, help_text='Specify the url to your product.', null=True, blank=True)
	body = models.TextField()
	category = models.ForeignKey(Category, related_name='category')
	mainImage = models.ImageField(blank=False, null=False, upload_to="media")
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	rating = RatingField(range=5)
	purchased = models.IntegerField(validators=[MinValueValidator(0)], )#add default=0 !!!
	viewed = models.IntegerField(validators=[MinValueValidator(0)], default=0)
	price = models.FloatField(validators=[MinValueValidator(0.01)])
	discountPrice = models.FloatField(validators=[MinValueValidator(0),], default=0, help_text="Put the new price")
	dateCreated = models.DateTimeField(default=timezone.now)
	specialOffer = models.BooleanField(default=False, help_text='Checking this will make it a special offer')
	active = models.BooleanField(default=True)
	quantity = models.IntegerField(validators=[MinValueValidator(0)], default=0)
	tags = models.CharField(max_length=500)

	def get_sell_price(self):
		if discount < price:
			return discount
		else:
			return None


	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Product, self).save(*args, **kwargs)

	def display_image(self):
		return mark_safe("<img height='200' src='/media/%s'>" % self.mainImage)
	display_image.allow_tags = True

class Images(models.Model):
	title = models.CharField(max_length=300)
	image = models.ImageField(blank=False, null=False, upload_to="media")
	product = models.ForeignKey(Product)
	dateCreated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


@receiver(pre_delete, sender=Product)
def product_delete(sender, instance, **kwargs):
	if(instance.mainImage is not None):
		instance.mainImage.delete(False)
	else:
		return "error"