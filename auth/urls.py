from django.conf.urls import patterns

urlpatterns = patterns('auth.views',
    (r'^login/','login_user'),
    (r'^register/','register'),
)
