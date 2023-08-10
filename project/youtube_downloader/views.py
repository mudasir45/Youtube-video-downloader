# youtube_downloader/views.py
from django.shortcuts import render
from django.http import JsonResponse
from pytube import YouTube
import os
from django.conf import settings

def download_360p_mp4_videos(url: str, outpath: str = "downloads/"):
    yt = YouTube(url)
    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(os.path.join(settings.MEDIA_ROOT, outpath))


def download_youtube_video(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        print(video_url)
        download_360p_mp4_videos(video_url)
            
        response_data = {
        'status': 'success',
        'message': 'Video downloaded successfully.',
        }
            
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})


def home(request):
    return render(request, 'index.html')