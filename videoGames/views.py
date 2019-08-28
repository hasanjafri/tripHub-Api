from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import VideoGamePOI


def index(request):
    latest_video_game_poi_list = VideoGamePOI.objects.all()
    context = {'latest_video_game_poi_list': latest_video_game_poi_list}
    return render(request, 'videoGames/index.html', context)


def details(request, video_game_poi_id):
    video_game_poi = get_object_or_404(VideoGamePOI, pk=video_game_poi_id)
    return render(request, 'videoGames/details.html', {'video_game_poi': video_game_poi})


def ratings(request, video_game_poi_id):
    response = "You're looking at the ratings of VideoGamePOI: %s."
    return HttpResponse(response % video_game_poi_id)


def rate(request, video_game_poi_id):
    return HttpResponse("You are rating VideoGamePOI: %s." % video_game_poi_id)
