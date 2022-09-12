# TODO: Implement Routings Here
from django.urls import path
from katalog.views import takeData

app_name = 'katalog'

urlpatterns = [
    path('', takeData, name='takeData'),
]