from django.shortcuts import render

from django.http import HttpResponse , HttpResponseRedirect

from .models import Verify
#from .forms import VerifyForm,PastFormForm
# Create your views here.
#CRUD
def landing(request):
	return render(request, "landing.html",{})

def verify_create(request):
	form = VerifyForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#return HttpResponseRedirect(instance.get_absolute_url( ))
	context = {
		"form" : form,
	}
	return render(request, "form.html",context)

def form_create(request):
	form = PastFormForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		"form" : form,
	}
	return render(request, "elements.html",context)
import datetime, pytz, requests

def API_create(request):
	get_params = request.GET
	if 'error' in get_params:
	    raise ValueError('Error authorizing application: %s' % get_params[error])
	response = requests.post('https://drchrono.com/o/token/', data={
	    'code': get_params['code'],
	    'grant_type': 'authorization_code',
	    'redirect_uri': 'http://127.0.0.1:5000/',
	    'client_id': 'IIwlCkabMhCjJHRbjfbalUnCosjMBdIOqsfWQRMZ',
	    'client_secret': '7SsQ4utFnRWNXP547EFhXlqExYSk3Bjq3zbSLHVxuWtqE6AX4hpFmpxqlH84wJON1vf2ymRaQlomKSZxmFCv9JZbb4sVB9M6OxbYmC0G8DwakIVuAtcSuXbCwUpFjgzp',
	})
	response.raise_for_status()
	data = response.json()

	# Save these in your database associated with the user
	access_token = data['access_token']
	refresh_token = data['refresh_token']
	expires_timestamp = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])
	
	request.session['access_token'] = access_token
	request.session['refresh_token'] = refresh_token
	print "this is what you are looking for : " , request.session['access_token']
	return render(request, "loading.html",{})

def play_with_api(request):
	access_token = request.session['access_token']

	headers = {
	    'Authorization': 'Bearer ' + str(access_token),
	}

	patients = []
	i = 0 
	patients_url = 'https://drchrono.com/api/patients'
	string = "<ul>"
	while patients_url:
		response = requests.get(patients_url, headers=headers)
		response.raise_for_status()
		print response.content
		data = response.json()
		patients.extend(data['results'])
		patients_url = data['next'] # A JSON null on the last page
		string = string + "<li>"+str(patients[0])+"</li>"
		i = i + 1
	# context = {
	# 			"patients" : patients
	# }

	string = string + "</ul>"
	for patient in patients:
		flag = True 
		#if ((patient.updated_at > .updated_at ) & (len(Verify.objects.filter(uid=patient.id))>0)) | (len(Verify.objects.filter(uid=patient.id))==0)
		if (len(Verify.objects.filter(uid=patient.id))>0):
			if (patient.updated_at <= Verify.objects.filter(uid=patient.id).updated_at ):
				flag = False
		if flag:
			instance =  Verify()
			instance.uid = patient.id
			instance.first_name = patient.first_name
			instance.last_name = patient.last_name
			instance.dob = patient.date_of_birth
			instance.email = patient.email
			#instace.sex = patient.sex
			instace.appointment = patient.date_of_last_appointment
			instance.save()


	instance = Verify.objects.all()
	context = {
	 			"patients" : instance
	}			
	return render(request, "list.html",context)
