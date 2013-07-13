# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

def index(req):
	return HttpResponse("hello world,welcomle to our domain")

