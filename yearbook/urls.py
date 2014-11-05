from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yearbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'book.views.home', name='home'),
    url(r'^users$', 'book.views.users', name='users'),
    url(r'^signup$', 'book.views.signup', name='signup'),
    url(r'^login$', 'book.views.login', name='login'), 
    url(r'^logout$', 'book.views.logout', name='logout'), 
    url(r'^admin/', include(admin.site.urls)),
)
