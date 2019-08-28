from django.urls import path

from . import views

app_name = 'videoGames'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:video_game_poi_id>/', views.details, name="details"),
    path('<int:video_game_poi_id>/ratings/', views.ratings, name="ratings"),
    path('<int:video_game_poi_id>/rate/', views.rate, name="rate")
]
