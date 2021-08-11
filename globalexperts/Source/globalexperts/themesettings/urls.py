from django.urls import include, path,re_path
from django.contrib.auth.decorators import login_required

app_name = 'themesettings'

from . import views

urlpatterns = [
	 re_path('sample', views.foo, name='sample'),
]