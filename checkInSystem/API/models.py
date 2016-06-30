from __future__ import unicode_literals

from django.db import models

# Create your models here.
class API_class(models.Model):
	def __unicode__(self):
		return self