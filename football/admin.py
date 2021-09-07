from django.contrib import admin

# Register your models here.

from .models import Player, Club, Fixture

admin.site.register(Club)
admin.site.register(Fixture)
admin.site.register(Player)