from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
class UserForm(forms.Form):
    long_url = forms.CharField()
	short_url = forms.CharField()
def index(req):

    if req.method == 'POST':
	    uf = UserForm(req.POST)
		if uf.is_valid():
		    long_url = uf.cleaned_data['short_url']
			short_url = hashlib.sha1(long_url).hexdigest()
			short_url = short_url[:8]
			return render_to_response('index.html',{'uf':uf,})

	return render_to_response("index.html",{'uf':uf})
 


    

