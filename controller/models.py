from django.db import models

# Create your models here.

class Slide(models.Model):
	title=models.CharField(max_length=120)
	body = models.TextField()
	image = models.ImageField(blank=False, null=False)
	created = models.DateTimeField(auto_now_add=True)
	display = models.BooleanField(default=True)

	def __str__(self):
		return self.title