#-*-coding:utf8-*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response 
from django import forms
from bit.models import Url
import hashlib

class UrlForm(forms.Form):
    long_url = forms.CharField(max_length = 200)

def index(req):
    if req.method == "POST":
        lu = UrlForm(req.POST)
        if lu.is_valid():
            long_url = lu.cleaned_data["long_url"]
            longx_url = hashlib.md5(long_url).hexdigest()
            short2_url = longx_url[0:8]
            user = Url.objects.filter(long_url__exact = long_url)
            if user:
                full_long_url= user[0].long_url
                if full_long_url[0:4] == "http":
                    return HttpResponseRedirect(full_long_url)
                else:
                    return HttpResponseRedirect("http://%s"%full_long_url)
            else:
                url= Url.objects.create(long_url=long_url,short_url=short2_url)
                print url
                return HttpResponse("short_url:%s:and:%s"%(url,short2_url))
    else:
        lu = UrlForm()
    return render_to_response('index.html',{'lu':lu})

def turn(req,short):
    long_url = Url.objects.filter(short_url__exact = short)
    full_long_url= long_url[0].long_url
    if full_long_url[0:4] == "http":
        return HttpResponseRedirect(full_long_url)
    else:
        return HttpResponseRedirect("http://%s"%full_long_url)
    




