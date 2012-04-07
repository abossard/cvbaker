from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import datetime

def home(request):
    now = datetime.datetime.now()
    return render_to_response('base_home.html', locals(), context_instance=RequestContext(request))
