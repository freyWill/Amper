from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
	user = models.ForeignKey(User)

	def __str__(self):
		return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)



post_save.connect(create_user_profile, sender=User)