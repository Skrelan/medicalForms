from django import forms

from .models import Verify

class VerifyForm(forms.ModelForm):
	class Meta:
		model = Verify
		fields = [
			"name",
			"dob"
		]
class PastFormForm(forms.ModelForm):
	class Meta:
		model = Verify
		fields = [ "ssn","appointment","allergies","pastMedication","sex","sign"]		