#-*-coding:utf8-*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response 
from django import forms
from bit.models import Url
import hashlib
from bit.def_url import judgment, shortTo, shortToLong

class UrlForm(forms.Form):
    long_url = forms.CharField(max_length=200)

def index(req):
    if req.method == "POST":
        lu = UrlForm(req.POST)
        if lu.is_valid():
            #判断长url是否有http://
            #judgment(lu)
            long_url = judgment(lu)             
            db_url = Url.objects.filter(long_url__exact=long_url)
            if db_url:
		        short_url = db_url[0].short_url
            else:
                short_url = shortTo(long_url)
            return render_to_response('index.html', {'lu':lu, 'short_url':short_url, 'long_url':long_url})
    else:
        lu = UrlForm()
    return render_to_response('index.html', {'lu':lu})

def turn(req, short_hash):
    full_long_url = shortToLong(short_hash)
    return HttpResponseRedirect(full_long_url)
