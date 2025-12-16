from django.shortcuts import render

from music.models import Song


def home(request):
    songs = Song.objects.all().order_by('-created_at')
    context = {
        'songs' : songs
    }

    print("--------------------------------------------------")
    print(f"تعداد آهنگ‌های پیدا شده: {songs.count()}")
    print(songs)
    print("--------------------------------------------------")
    return render(request, 'music/home.html', context)
