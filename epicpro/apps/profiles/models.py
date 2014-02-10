from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User)
	image = models.ImageField(upload_to='profile_image')
	can_create_material = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s" % (self.user.username,)