from django.shortcuts import render

from django.http import HttpResponse , HttpResponseRedirect
from .models import PastForm
from .forms import PastFormForm
# Create your views here.
def form_create(request):
	form = PastFormForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#return HttpResponseRedirect(instance.get_absolute_url( ))
	context = {
		"form" : form,
	}
	return render(request, "elements.html",context)
