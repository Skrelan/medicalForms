from django import forms

from .models import Verify

class VerifyForm(forms.ModelForm):
	class Meta:
		model = Verify
		fields = [
			"first_name",
			"last_name",
			"dob"
		]
class PastFormForm(forms.ModelForm):
	class Meta:
		model = Verify
		fields = [ "email","uid","appointment"]		