from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^comments/',include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blogme.urls')),
    url(r'^auth/',include('auth.urls')),
)
from django.conf import settings
if settings.DEBUG: 
        urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH, 'show_indexes':True}),) 
