from django import forms

from .models import PastForm

class PastFormForm(forms.ModelForm):
	class Meta:
		model = PastForm
		fields = [ "ssn","appointment","allergies","pastMedication","sex","sign"]