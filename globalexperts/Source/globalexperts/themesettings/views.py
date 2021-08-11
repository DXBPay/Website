from django.shortcuts import render
from django.shortcuts import render_to_response

from company.models import Company

def foo(request,):
	 return render_to_response("default_theme/base/sample.html")
