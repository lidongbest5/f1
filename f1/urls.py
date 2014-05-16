from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from guess.views import *
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'f1.views.home', name='home'),
    # url(r'^f1/', include('f1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^f1/admin/', include(admin.site.urls)),
    (r'^f1/$',showIndex),
    (r'^f1/login/',login),
    (r'^f1/logout/',logout),
    (r'^f1/sign/',sign),
    (r'^f1/submit/',submit),
    (r'^f1/total/',total),
    (r'^f1/root/',root),
    (r'^f1/test/',test),
    (r'^f1/history/',history),
    (r'^f1/findHistory/',findHistory),
    (r'^f1/change/',change),
    (r'^f1/changeSave/',changeSave),
    (r'^f1/findUser/',findUser),
    (r'^f1/setContent/',setContent),
    (r'^f1/setContact/',setContact),
    (r'^f1/showPre/',showPre),
    (r'^f1/setRe/',setRe),
    (r'^f1/setResult/',setResult),
    (r'^f1/races/(\d+)/$',showRaces),
)
urlpatterns += patterns('',
    url(r'^f1/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
