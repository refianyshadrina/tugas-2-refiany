from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    return render(request, 'mywatchlist.html', context)

data_watchlist = WatchList.objects.all()
context = {
    'watchlist_data': data_watchlist,
    'nama': 'Refiany Shadrina',
    'npm' : 2106650185
}

def show_byhtml(request):
    return render(request, 'watchedListData.html', contextHtml)

contextHtml = {
    'watchlist_data': data_watchlist
}

def show_byxml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_byjson(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")