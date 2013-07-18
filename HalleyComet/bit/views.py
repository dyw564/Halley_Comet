from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response 
from django import forms
from bit.models import Url
import hashlib
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class UrlForm(forms.Form):
    long_url = forms.CharField(max_length=200)

class UserRegistForm(forms.ModelForm):
    email = forms.CharField()
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'password': forms.PasswordInput()
        }

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

def user_regist(req):
    if req.method == "POST":
        uf = UserRegistForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            password = hashlib.sha1(password).hexdigest()
            email = uf.cleaned_data['email']
            user = User.objects.create_user(username=username,password=password,email=email)
            user.is_staff = True
            user.save()
            if user:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserRegistForm()
    return render_to_response('regist.html',{'uf':uf})

def user_login(req):
    if req.method == "POST":
        lf = UserLoginForm(req.POST)
        if lf.is_valid():
            username = lf.cleaned_data['username']
            password = lf.cleaned_data['password']
            password = hashlib.sha1(password).hexdigest()
            user = authenticate(username=username,password=password)
            if user:
                login(req,user)
                return HttpResponseRedirect('/index/')
            else :
                return HttpResponseRedirect('/login/')
    else :
        lf = UserLoginForm()
    return render_to_response('login.html',{'lf':lf})

def user_logout(req):
    logout(req)
    return HttpResponseRedirect('/index/')

def index(req):
    if req.method == "POST":
        lu = UrlForm(req.POST)
        if lu.is_valid():
            long_url = lu.cleaned_data["long_url"]
            db_url = Url.objects.filter(long_url__exact=long_url)
            if db_url:
		        short_url = db_url[0].short_url
            else:
                longx_url = hashlib.md5(long_url).hexdigest()
                short_url = "localhost:8000/%s"%longx_url[0:8]
                url= Url.objects.create(long_url=long_url,short_url=short_url)
                if long_url[:4] != 'http':
                    long_url = 'http://'+long_url
            return render_to_response('index.html',{'lu': lu, 'short_url': short_url, 'long_url': long_url})
    else:
        lu = UrlForm()
    return render_to_response('index.html',{'lu': lu})

def turn(req,short_hash):
    short = "localhost:8000/%s" % short_hash
    long_url = Url.objects.filter(short_url__exact=short)
    full_long_url = long_url[0].long_url

    if full_long_url[0:4] != "http":
    	full_long_url = "http://"+full_long_url
    return HttpResponseRedirect(full_long_url)
