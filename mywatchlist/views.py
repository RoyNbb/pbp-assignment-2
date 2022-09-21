from django.shortcuts import render
from mywatchlist.models import Movies
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
data = Movies.objects.all()
def show_watchlist(request):
    context = {
        'list_movies': data ,
        'name' : 'Roy Maruli Tua Nababan',
        'id' : '2106750521'
    }
    return render(request, 'watchlist.html', context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
