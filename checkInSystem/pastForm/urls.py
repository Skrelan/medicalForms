from django.conf.urls import url
from django.contrib import admin

from .views import (
    form_create,
	)

urlpatterns = [
    url(r'create/',form_create, name='page2' ),
    #url(r'^posts/$', "<appname>.views.<function_name>)",
]
