# melody_madness
UMBC CMSC 447 Group Project

The Melody Madness project should be run on PyCharm with a virtual environment. It is ideal to run this project using Python 3.9 or higher.

Please view the `requirements.txt` file found in the root of this directory for which libraries are required.
### Running the webapp
- To run the application on PyCharm with Django, enter `python manage.py runserver` into the command line.
  - To access the website, access the URL `http://localhost:8000/`
  - It is necessary that Spotify API secrets be copied and pasted within `spauth(request)` found in `spotify_auth/views.py` in order to authorize with the Melody Madness Spotify app, and pull artists using a Spotify account.
- Accessing the main URL will send you to a Welcome page. To log in with Spotify, click the "Login With  Spotify" button and log in with your Spotify credentials.
  - Melody Madness will provide you with the information that will be pulled from your Spotify account before you give permission to authorize the app.
- To view the bracket, you will be automatically redirected to the `generate` URL. You must click the `Generate my Bracket` button to display the bracket with your Spotify artists.

### Testing
- To run the url and view unit tests, enter `python manage.py test` into the command line.

### Functionality
- Note that functionality of the bracket is not complete! Voting sometimes behaves in unexpected ways.

