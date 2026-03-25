from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', views.index),
    path('genres/', views.genres),
    path('tracks/', views.tracks),
    path('artists/', views.artists),
    path('add_genre/', views.add_genre),
    path('editgenre/<int:id_genre>', views.edit_genre),
    path('deletegenre/<int:id_genre>', views.delete_genre),
    path('add_track/', views.add_track),
    path('edittrack/<int:id_track>', views.edit_track),
    path('deletetrack/<int:id_track>', views.delete_track),
    path('add_artist/', views.add_artist),
    path('editartist/<int:id_artist>', views.edit_artist),
    path('deleteartist/<int:id_artist>', views.delete_artist),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

