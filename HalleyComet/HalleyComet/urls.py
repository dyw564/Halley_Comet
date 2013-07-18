from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HalleyComet.views.home', name='home'),
    # url(r'^HalleyComet/', include('HalleyComet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r"^index/$","bit.views.index"),
    url(r"^(\w{8})/$","bit.views.turn"),
    url(r'regist/$','bit.views.user_regist'),
    url(r'login/$','bit.views.user_login'),
    url(r'logout/','bit.views.user_logout'),
)
