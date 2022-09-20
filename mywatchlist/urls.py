from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_byxml
from mywatchlist.views import show_byjson
from mywatchlist.views import show_byhtml

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('xml/', show_byxml, name='show_byxml'),
    path('json/', show_byjson, name='show_byjson'),
    path('html/', show_byhtml, name='show_byhtml'),

]