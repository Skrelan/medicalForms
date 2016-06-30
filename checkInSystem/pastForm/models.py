from __future__ import unicode_literals
from django.db import models
import os
from django.core.urlresolvers import reverse

# Create your models here.

class PastForm(models.Model):
	Male = 'M'
	Female = 'F'
	Other = 'O'
	gender_choices = ((Male,'Male'),
		(Female,'Female'),
		(Other,'Other'),
		)
	ssn = models.DecimalField(max_digits=8,decimal_places=0)
	appointment = models.DateTimeField(auto_now=False, auto_now_add=False)
	allergies = models.CharField(max_length = 180) 
	pastMedication = models.CharField(max_length = 180)
	sex = models.CharField(max_length=2,choices=gender_choices,default=Male)
	sign =  models.CharField(max_length=120)
	def __unicode__(self):
		return self.sign