# TODO: Implement Routings Here
from django.urls import path
from katalog.views import takeData


urlpatterns = [
    path('', takeData, name='takeData'),
]