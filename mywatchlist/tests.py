
# Create your tests here.
from multiprocessing.connection import Client
from django.test import TestCase, Client
from django.urls import reverse

class test(TestCase):
    def testHtml(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_byhtml"))
        self.assertEquals(response.status_code,200)

    def testJSON(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_byjson"))
        self.assertEquals(response.status_code,200)

    def testXML(self):
        client = Client()
        response = client.get(reverse("mywatchlist:show_byxml"))
        self.assertEquals(response.status_code,200)
# Create your tests here.
