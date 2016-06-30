from django import forms

from .models import Verify

class VerifyForm(forms.ModelForm):
	class Meta:
		model = Verify
		fields = [
			"name",
			"dob"
		]