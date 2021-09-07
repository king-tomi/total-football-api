from django.db import models

# Create your models here.
class Fixture(models.Model):

    home_team = models.CharField(max_length=250)
    away_team = models.CharField(max_length=250)
    home_goals = models.IntegerField()
    away_goals = models.IntegerField()
    winner = models.CharField(max_length=250)
    yellow_cards = models.IntegerField(null=True, blank=True)
    red_cards = models.IntegerField(null=True, blank=True)
    free_kicks = models.IntegerField(null=True, blank=True)
    penalties = models.IntegerField(null=True, blank=True)
    corners = models.IntegerField(null=True, blank=True)
    home_possession = models.IntegerField(null=True, blank=True)
    away_possession = models.IntegerField(null=True, blank=True)
    home_shots = models.IntegerField(null=True, blank=True)
    away_shots = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.home_team} {self.home_goals} - {self.away_goals} {self.away_team}"

class Club(models.Model):

    name = models.CharField(max_length=250)
    stadium = models.CharField(max_length=250, blank=True, unique=True)
    position = models.PositiveIntegerField(null=True, blank=True)

class Player(models.Model):

    name = models.CharField(max_length=250)
    age = models.CharField(max_length=100)
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    goals = models.IntegerField(null=True, blank=True)
    assists = models.IntegerField(null=True, blank=True)
    yellows = models.IntegerField(null=True, blank=True)
    reds = models.IntegerField(null=True, blank=True)
    shots = models.IntegerField(null=True, blank=True)
    passes = models.IntegerField(null=True, blank=True)
    dribbles = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"