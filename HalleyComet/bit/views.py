#-*-coding:utf8-*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from bit.models import Url
from django.contrib.auth import authenticate, login, logout
from bit.def_url import short_to_long, long_to_short

class UrlForm(forms.Form):
    long_url = forms.CharField(max_length=200)

class UserRegistForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

def user_regist(req):
    if req.method == "POST":
        uf = UserRegistForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.create_user(username=username,password=password)
            user.save()
            return HttpResponse()
    else:
        uf = UserRegistForm()
    return render_to_response('regist.html', {'uf':uf})
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


