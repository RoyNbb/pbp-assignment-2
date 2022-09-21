from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
data = MyWatchList.objects.all()
def show_watchlist(request):
    movies_watched = 0
    movies_count = 0
    for movie in data:
        movies_count +=1
        if movie.watched:
            movies_watched += 1
    watch_prompt = "Wah, kamu masih sedikit menonton!"
    if movies_watched > movies_count/2:
        watch_prompt = "Selamat, kamu sudah banyak menonton!"
    
    context = {
        'list_movies': data ,
        'name' : 'Roy Maruli Tua Nababan',
        'id' : '2106750521',
        'watch_prompt' : watch_prompt
    }
    return render(request, 'watchlist.html', context)

def show_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")




    