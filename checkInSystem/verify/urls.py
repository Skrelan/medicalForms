from django.conf.urls import url
from django.contrib import admin

from .views import (
    verify_create,
    verify_update,
    verify_delete,
	)

urlpatterns = [
    url(r'',verify_create),
    #url(r'^posts/$', "<appname>.views.<function_name>)",
]
