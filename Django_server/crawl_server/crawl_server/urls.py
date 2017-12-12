from django.conf.urls import patterns, include, url
#from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crawl_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'crawl_job', include(r'crawl_job.urls'))
)
