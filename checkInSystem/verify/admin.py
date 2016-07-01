from django.contrib import admin
from verify.models import Verify
from API.models import API_class

# Register your models here.
class VerifyAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','last_name','dob']
	list_display_links = ['__unicode__']
	class Meta:
		models = Verify
admin.site.register(Verify, VerifyAdmin)
