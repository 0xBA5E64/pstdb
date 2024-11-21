from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Episode

# Create your views here.

#def index(request):
#    return HttpResponse("PSTDB Index page.")

def episode_index(request):
    episodes = Episode.objects.all()
    context = {
        "episodes": episodes
    }
    template = loader.get_template("podcast/episode_index.html")
    return HttpResponse(template.render(context, request))