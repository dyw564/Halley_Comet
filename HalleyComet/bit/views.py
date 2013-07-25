#-*-coding:utf8-*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response 
from django import forms
from bit.models import Url
import hashlib
from bit.def_url import short_to_long,long_to_short

class UrlForm(forms.Form):
    long_url = forms.CharField(max_length=200)

def index(req):
    if req.method == "POST":
        lu = UrlForm(req.POST)
        if lu.is_valid():
            #判断长url是否有http://
            #judgment(lu)
            long_url = lu.cleaned_data["long_url"]
            short_url = long_to_short(long_url)
            return render_to_response('index.html', {'lu': lu, 'short_url': short_url, 'long_url': long_url})
    else:
        lu = UrlForm()
    return render_to_response('index.html', {'lu':lu})

def turn(req, short_hash):
    full_long_url = shortToLong(short_hash)
    return HttpResponseRedirect(full_long_url)
