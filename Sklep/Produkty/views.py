from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty,Kategoria

def index(request):
    wszystkie = Produkty.objects.all()
    jeden     = Produkty.objects.get(pk=4)
    kat       = Produkty.objects.filter(kategoria=2)
    producent = Produkty.objects.filter(producent=2)
    kat_name  = Kategoria.objects.get(pk=1)
    null      = Produkty.objects.filter(kategoria__isnull=True)
    zawiera   = Produkty.objects.filter(opis__icontains="mysz")
    return HttpResponse(wszystkie)
