from django.conf.urls import include, url
#from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'crawl_job', include(r'crawl_job.urls'))
]






