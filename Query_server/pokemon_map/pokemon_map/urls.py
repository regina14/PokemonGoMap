from django.conf.urls import url, include

urlpatterns = [
    url(r'map', include(r'map.urls'))
]

