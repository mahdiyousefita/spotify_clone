from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from music.forms import SignUpForm
from music.models import Song, Artist


def home(request):
    query = request.GET.get('q')

    songs = Song.objects.all().order_by('-created_at')

    if query:
        songs = songs.filter(
            Q(title__icontains=query) | Q(album__artist__name__icontains=query)
        )
    context = {
        'songs' : songs,
        'query' : query
    }
    return render(request, 'music/home.html', context)



from django.shortcuts import render

def dashboard(request):
    return render(request, 'music/dashboard.html')




def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)

    songs = Song.objects.filter(album__artist=artist).order_by('-created_at')

    context = {
        'artist' : artist,
        'songs': songs
    }

    return render(request, 'music/artist_detail.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'music/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'music/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
