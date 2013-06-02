from django.conf.urls import patterns, include, url
from liveinfo import views
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	url(r'^mainpage$', 'liveinfo.views.mainView'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^index$', 'liveinfo.views.indexView'),
    # Examples:
    # url(r'^$', 'vatan.views.home', name='home'),
    # url(r'^vatan/', include('vatan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
