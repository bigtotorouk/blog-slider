from django.conf.urls import patterns, url

urlpatterns = patterns('blogme.views',
    url(r'^$', 'index'),
    (r'^post/(?P<year>\d{4})/$','archive_year'),
    url(r'^post/(?P<postId>\d)/','post_view',name='post_view'),
)
