#-*-coding:utf8-*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from bit.models import Url
from bit.def_url import short_to_long, long_to_short

class UrlForm(forms.Form):
    long_url = forms.CharField(max_length=200)

def index(req):
    if req.method == "POST":
        lu = UrlForm(req.POST)
        if lu.is_valid():
            long_url = lu.cleaned_data["long_url"]
            short_url = long_to_short(long_url)
            return render(req, 'index.html', {'lu': lu, 'short_url': short_url, 'long_url': long_url})
    else:
        lu = UrlForm()
    return render(req, 'index.html', {'lu':lu}) 

def turn(req, short_hash):
    full_long_url = short_to_long(short_hash)
    return HttpResponseRedirect(full_long_url)


