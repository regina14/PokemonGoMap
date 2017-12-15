from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'pokemon', views.pokemons, name='pokemons')
]
