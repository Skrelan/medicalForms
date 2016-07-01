from __future__ import unicode_literals
from django.db import models
import os
from django.core.urlresolvers import reverse

# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Verify(models.Model):
	#image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	fist_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	dob = models.DateField(auto_now=False, auto_now_add=False)
	email = models.CharField(max_length=180)
	uid = models.DecimalField(max_digits=10,decimal_places=0)
	# Male = 'M'
	# Female = 'F'
	# Other = 'O'
	# name = models.CharField(max_length=120)
	# gender_choices = ((Male,'Male'),
	# 	(Female,'Female'),
	# 	(Other,'Other'),
	# 	)
	#ssn = models.DecimalField(max_digits=8,decimal_places=0)
	appointment = models.DateTimeField(auto_now=False, auto_now_add=False)
	#allergies = models.CharField(max_length = 180) 
	#pastMedication = models.CharField(max_length = 180)
	#sex = models.CharField(max_length=2,choices=gender_choices,default=Male)
	#sign =  models.CharField(max_length=120)
	def __unicode__(self):
		return self.last_name