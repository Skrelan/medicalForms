from django.conf.urls import url
from django.contrib import admin

from .views import (
    verify_create,
    form_create,
    landing,
    API_create,
    play_with_api,
	)

urlpatterns = [
    url(r'verify',verify_create),
    url(r'form',form_create),
    url(r'landing',landing),
    url(r'^$',API_create),
    url(r'list',play_with_api)
    #url(r'^posts/$', "<appname>.views.<function_name>)",
]
