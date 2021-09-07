from django.test import TestCase
from .models import Club, Player, Fixture

# Create your tests here.

class ClubTest(TestCase):

    def setUp(self) -> None:
        Club.objects.create(name="Real Madrid CF")

    def test_club(self):
        club = Club.objects.get(id=1)
        self.assertEqual(club.name, "Real Madrid CF")