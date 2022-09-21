from django.shortcuts import render
from mywatchlist.models import Film
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_film(request):
    data_film = Film.objects.all()
    context = {
        'list_film' : data_film,
        'nama' : 'Muhammad Rafi Adiwibowo',
        'id' : '2106653855',
    }
    return render(request, "mywatchlist.html", context)

def film_xml(request):
    data = Film.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def film_json(request):
    data = Film.objects.all()    
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(requst, id):
    data = Film.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(requst, id):
    data = Film.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    
