from django.contrib import admin
from django.urls import path

from .views import ClubsView, ClubByNameView, PlayersView,  PlayerByNameView, FixtureView, FixtureByWinnerView

urlpatterns = [
    path('clubs/', ClubsView.as_view()),
    path('players/', PlayersView.as_view()),
    path('fixtures/', FixtureView.as_view()),
    path('clubs/<str:name>', ClubByNameView.as_view()),
    path('players/<str:name>', PlayerByNameView.as_view()),
    path('fixtures/<str:winner>', FixtureByWinnerView.as_view())
]