from django.shortcuts import render
from rest_framework import generics
from .models import Club, Fixture, Player
from .serializers import ClubSerializer, FixtureSerializer, PlayerSerializer

# Create your views here.

class ClubsView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class PlayersView(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class FixtureView(generics.ListAPIView):
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer

class ClubByNameView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    lookup_field = "name"
    serializer_class = ClubSerializer

class PlayerByNameView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    lookup_field = "name"
    serializer_class = PlayerSerializer


class FixtureByWinnerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fixture.objects.all()
    lookup_field = "winner"
    serializer_class = FixtureSerializer