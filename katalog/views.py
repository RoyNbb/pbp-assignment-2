from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem

def show_catalog(request):
    catalogs = CatalogItem.objects.all()
    context = {
        'list_catalog': catalogs ,
        'name' : 'Roy Maruli Tua Nababan',
        'id' : '2106750521'
    }
    return render(request, 'katalog.html', context)

