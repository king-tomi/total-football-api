from rest_framework import fields, serializers

from .models import Club, Fixture, Player

class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = ('id','name', 'stadium')

class FixtureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fixture
        fields = ('home_team', 'away_team', 'home_goals', 'away_goals', 'winner')

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('name', 'age', 'club', 'goals', 'assists')