from django.shortcuts import render

from django.http import HttpResponse , HttpResponseRedirect

from .models import Verify
from .forms import VerifyForm
# Create your views here.
#CRUD
def verify_create(request):
	# if request.method == "POST":
	# 	print request.POST.get("name")
	# 	print request.POST.get("dob")
	form = VerifyForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#return HttpResponseRedirect(instance.get_absolute_url( ))
	context = {
		"form" : form,
	}
	return render(request, "form.html",context)

def verify_list(request):
	return HttpResponse("<h1>Lists</h1>")

def verify_update(request):
	return HttpResponse("<h1>Update</h1>")

def verify_delete(request):
	return HttpResponse("<h1>Delete</h1>")
