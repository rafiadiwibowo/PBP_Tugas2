# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import film_json, film_xml, show_json_by_id, show_xml_by_id
from mywatchlist.views import show_film

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_film, name='show_mywatchlist'),
    path('html/', show_film, name='show_mywatchlist'),
    path('xml/', film_xml, name='watchlist_xml'),
    path('json/', film_json, name='watchlist_json'),
    path('json/<int:id>', show_json_by_id, name='show_jason_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]   