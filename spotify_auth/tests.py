#tests.py for auth
from django.test import TestCase
from spotify_auth.models import Artist
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

class SPDataTests(TestCase):
    def test_create_artist(self):
        #test artist object & save
        name = "Test Artist"
        uri = "spotify:artist:URI-VALUES-GO-HERE"
        genre = "music"
        pop = 100
        img = "https://i.imgur.com/1uZW1SD.jpg"

        artist = Artist(artist=str(name), a_uri=str(uri), a_genre=str(genre), a_pop=int(pop), a_img=str(img))
        artist.save()

        # check if the test object exists
        self.assertTrue(len(Artist.objects.filter(artist="Test Artist")) > 0, msg="Test Artist saved")

    def test_delete_artist(self):
        artist = Artist.objects.filter(artist="Test Artist")
        artist.delete()

        self.assertEquals(len(Artist.objects.filter(artist="Test Artist")), 0, msg="Test artist deleted")

    def test_top_artists(self):

        #should fail w/o cid & secret
        CID = ""
        SECRET = ""
        REDIR_URL = 'http://localhost:8888/callback'

        oauth = SpotifyOAuth(client_id=CID, client_secret=SECRET, redirect_uri=REDIR_URL, scope='user-top-read')
        sp_auth = spotipy.Spotify(auth_manager=oauth)
        result = sp_auth.current_user_top_artists(limit=16, offset=0, time_range='long_term')
        vals = result['items']

        try:
            os.remove('.cache')
        except OSError:
            pass

        self.assertEquals(len(vals), 16)