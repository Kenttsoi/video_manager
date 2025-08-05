from django.shortcuts import render, get_object_or_404
from .models import Video, Actor

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    return render(request, 'video_detail.html', {'video': video})

def actor_detail(request, actor_id):
    actor = get_object_or_404(Actor, id=actor_id)
    videos = actor.videos.all()
    return render(request, 'actor_detail.html', {
        'actor': actor,
        'videos': videos
    })