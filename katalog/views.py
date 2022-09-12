from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def takeData(request):
    return render(request, 'katalog.html', context)

data_katalog = CatalogItem.objects.all()
context = {
    'list_katalog': data_katalog,
    'nama': 'Refiany Shadrina'
}