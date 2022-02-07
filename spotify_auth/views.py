# Alex Galetus & Ryan Kisner - CMSC 447 Fall 2021

from django.http import HttpResponse, HttpResponseRedirect
import os
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from .models import Artist

# ParseData(data)
# parses the raw JSON into data needed for the bracket. Data is stored in the Artist model -> db.
def ParseData(data):
    artists = []
    artists_uri = []
    artists_popularity = []
    artists_genres = []
    image_links = []

    # parses JSON into pandas dataframe
    for token in data:
        # Artist name
        artists_name = token['name']
        artists.append(artists_name)

        # Spotify URI for artist (eg: spotify:artist:xxx...)
        artist_uri = token['uri']
        artists_uri.append(artist_uri)

        # For image link indexing and image sizes. img[1] = 300x300 dimensions
        image_link = token['images'][1]['url']
        image_links.append(image_link)

        # Integer value Spotify API returns for an artist's popularity
        popularity = token['popularity']
        artists_popularity.append(popularity)

        # genre[0] = top genre selected for an artist, sometimes Spotify returns multiple genre options.
        genre = token['genres'][0]
        artists_genres.append(genre)

    # df setup
    artist_frame = pd.DataFrame(
        {
            'artist': artists,
            'artist_uri': artists_uri,
            'artists_genres': artists_genres,
            'artist_popularity': artists_popularity,
            'artist_image': image_links
        }
    )

    # artist obj creation
    artist_obj = Artist()

    # slow implementation, but we can get away with it given we're dealing with 16 artists or less
    for index, row in artist_frame.iterrows():
        artist_obj.artist = str(row['artist'])
        artist_obj.a_uri = str(row['artist_uri'])
        artist_obj.a_genre = str(row['artists_genres'])
        artist_obj.a_pop = int(row['artist_popularity'])
        artist_obj.a_img = str(row['artist_image'])
        artist_obj.save()
        artist_obj = Artist()

    # check if # artist objs is < 16 and add additional artists from a preset list
    # this would be the place to do it

    return

# redir(request)
def redir(request):
    # After Spotify authorization is complete & Artist objects are populated, move to /generate/ app
    return HttpResponseRedirect('/generate')

# spauth(request)
# Authenticates a user via the Spotify API & calls a parsing function that processes data needed for the bracket.
def spauth(request):
    CID = ''
    SECRET = ''
    resp = HttpResponse()

    # Gets user log in, collects their listening data, returns JSON file of that data
    REDIR_URL = 'http://localhost:8888/callback'

    # temp_list grabs data of top 16 sp artists (long term), user_creds grabs name, id, email from auth'd user
    temp_list = []
    # user_creds = []

    # This block authenticates user login via the API & grabs a temp token
    oauth = SpotifyOAuth(client_id=CID, client_secret=SECRET, redirect_uri=REDIR_URL, scope='user-top-read')
    sp_auth = spotipy.Spotify(auth_manager=oauth)

    # populates user's top 16 artists from raw json -> []
    if sp_auth:
        results = sp_auth.current_user_top_artists(limit=16, offset=0, time_range='long_term')
        for s in range(16):
            temp_list.append(results)

        # passing user info for login purposes (Not in use currently!)
        # resp.write(sp_auth.me())
        # user_res = sp_auth.me()
        # user_creds.append(user_res)

    else:
        # if authentication doesn't work, bad req
        resp = 400

    # data_list = top 16 artist data for a user
    data_list = temp_list[0]['items']

    # test to ensure raw json data is being correctly pulled via spotify API
    # with open('test.json', 'w', encoding='utf-8') as f:
    #     json.dump(results, f, ensure_ascii=False, indent=4)

    ParseData(data_list)

    # once a user is authenticated, token expiry = 1hr. that's an issue if
    # another user wants to log in before the expiry period is up for the
    # prev token. nuking .cache fixes this issue
    try:
        os.remove('.cache')
    except OSError:
        pass

    # If auth fails:
    if resp == 400:
        request = "CODE 400: Error. Spotify authorization did not succeed. Try again!"
    else:
        request = redir(request)

    return request