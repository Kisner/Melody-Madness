from django.contrib import admin
from spotify_auth.models import Artist
from tournament.models import Vote

# Register your models here.
admin.site.register(Artist)
admin.site.register(Vote)