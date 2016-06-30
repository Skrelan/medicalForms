from __future__ import unicode_literals
from django.db import models
import os
from django.core.urlresolvers import reverse

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Verify(models.Model):
	image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	name = models.CharField(max_length=120)
	dob = models.DateField(auto_now=False, auto_now_add=False) 
	#image = models.ImageField(upload_to=get_image_path,blank=True,null=True)
	def __unicode__(self):
		return self.name