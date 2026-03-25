from django.shortcuts import render, redirect
from .models import Genre, Track, Artist
from .forms import GenreForm, TrackForm, ArtistForm

# главная
def index(request):
    return render(request, 'index.html')

# жанры
def genres(request):
    # получим список жанров из базы
    g = Genre.objects.all()
    return render(request, 'genres.html', {'genres': g})

# треки
def tracks(request):
    # получим список треков из базы
    t = Track.objects.all()
    return render(request, 'tracks.html', {'tracks': t})

# исполнители
def artists(request):
    # получим список исполнителей из базы
    a = Artist.objects.all()
    return render(request, 'artists.html', {'artists': a})

# добавить жанр
def add_genre(request):
    # получили данные. нужно сохранить жанр в базу
    if request.method == "POST":
        # получаем данные из формы
        genre = GenreForm(request.POST)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    # это простой запрос, нужно показать форму
    else:
        genreform = GenreForm()
        return render(request, "add_genre.html", {'form': genreform})

# изменить жанр
def edit_genre(request, id_genre):
    # получим жанр, который нужно редактировать
    g = Genre.objects.get(id=id_genre)

    # получили данные. нужно сохранить жанр в базу
    if request.method == "POST":
        # получаем данные из формы
        genre = GenreForm(request.POST, instance=g)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    # это простой запрос, нужно показать форму
    else:
        genreform = GenreForm(instance=g)
        return render(request, "add_genre.html", {'form': genreform})
    
# удалить жанр
def delete_genre(request, id_genre):
    # получим жанр, который нужно удалить
    g = Genre.objects.get(id=id_genre)
    # удалим
    g.delete()
    return redirect('/genres')

# добавить трек
def add_track(request):
    # получили данные. нужно сохранить трек в базу
    if request.method == "POST":
        # получаем данные из формы
        track = TrackForm(request.POST, request.FILES)
        if track.is_valid():
            track.save()
        return redirect('/tracks')
    # это простой запрос, нужно показать форму
    else:
        form = TrackForm()
        return render(request, "add_track.html", {'form': form})
    
# изменить трек
def edit_track(request, id_track):
    # получим трек, который нужно редактировать
    t = Track.objects.get(id=id_track)

    # получили данные. нужно сохранить трек в базу
    if request.method == "POST":
        # получаем данные из формы
        track = TrackForm(request.POST, request.FILES, instance=t)
        if track.is_valid():
            track.save()
        return redirect('/tracks')
    # это простой запрос, нужно показать форму
    else:
        form = TrackForm(instance=t)
        return render(request, "add_track.html", {'form': form})

# удалить трек
def delete_track(request, id_track):
    # получим трек, который нужно удалить
    t = Track.objects.get(id=id_track)
    # удалим
    t.delete()
    return redirect('/tracks')

# добавить исполнителя
def add_artist(request):
    # получили данные. нужно сохранить трек в базу
    if request.method == "POST":
        # получаем данные из формы
        artist = ArtistForm(request.POST, request.FILES)
        if artist.is_valid():
            artist.save()
        return redirect('/artists')
    # это простой запрос, нужно показать форму
    else:
        form = ArtistForm()
        return render(request, "add_artist.html", {'form': form})
    
# изменить исполнителя
def edit_artist(request, id_artist):
    # получим исполнителя, который нужно редактировать
    a = Artist.objects.get(id=id_artist)

    # получили данные. нужно сохранить исполнителя в базу
    if request.method == "POST":
        # получаем данные из формы
        artist = ArtistForm(request.POST, request.FILES, instance=a)
        if artist.is_valid():
            artist.save()
        return redirect('/artists')
    # это простой запрос, нужно показать форму
    else:
        form = ArtistForm(instance=a)
        return render(request, "add_artist.html", {'form': form})

# удалить исполнителя
def delete_artist(request, id_artist):
    # получим исполнителя, которого нужно удалить
    a = Artist.objects.get(id=id_artist)
    # удалим
    a.delete()
    return redirect('/artists')