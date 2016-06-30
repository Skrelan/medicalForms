from django.conf.urls import url
from django.contrib import admin

from .views import (
    API_create,
    play_with_api,
	)

urlpatterns = [
    url(r'^$',API_create),
    url(r'^play/$',play_with_api),
    #url(r'^posts/$', "<appname>.views.<function_name>)",
]
