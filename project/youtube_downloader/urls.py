# youtube_downloader/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('download/', views.download_youtube_video, name='download_youtube_video'),
    path('', views.home, name='home'),
]
