from django.shortcuts import render
from django.http import HttpResponse
from .models import Band, Persons
#from django.template import loader
from django.http import Http404

# Create your views here.

def index(request):
    all_bands = Band.objects.all()
    return render(request, 'myblog/index.html', {'all_bands':all_bands,})
    #html = ''
    #for band in all_bands:
    #    url = '/myblog/' + str(band.id) + '/'
    #    html += '<a href="' + url + '">'+ band.name +'</a><br>'
    
    #template = loader.get_template('myblog/index.html')
    
    #return HttpResponse(template.render(context, request))
    

def persons(request,band_id):
    #return HttpResponse('<h2>Persons in band ' + str(band_id) + '</h2>')
    try:
        band = Band.objects.get(id=band_id)
    except Band.DoesNotExist:
        raise Http404("Band does not exist")
    return render(request, 'myblog/persons.html', {'band':band,})
    