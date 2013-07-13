#-*-coding:utf8-*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response 
from django import forms
import hashlib
class UrlForm(forms.Form):
    long_url = forms.CharField(max_length = 200)

def index(req):
    if req.method == "POST":
        lu = UrlForm(req.POST)
        if lu.is_valid():
            long_url = lu.cleaned_data["long_url"]
            short_url = hashlib.md5(long_url).hexdigest()
            short_url = short_url[0:8]
#            id = 290
#            value_url = (
#                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#                'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#                'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
#                'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
#                'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
#                'W', 'X', 'y', 'Z', '0', '1', '2', '3', 
#                '4', '5')
#            value = []
#            while id > 0:
#                url_id = id % 63;
#                 
#                value.append(url_id);
#                id = id/64
            return HttpResponse("short_url:%s"%short_url)
    else:
        lu = UrlForm()
    return render_to_response('index.html',{'lu':lu})

def lisi(req):
    return HttpResponseRedirect("http://www.baidu.com/")








