## README.md (spotify_auth)
Alex Galetus - CMSC 447, Fall 2021
###Spotify authorization flow & Artist models
- `spotify_auth` authorizes a user logging into Melody Madness via the Spotify API, and pulls artists from their account to populate a 16 "seeded" bracket.

- To run the application, you will need Django 3.2.8 (as of December 7th, 2021).
- Check the additional requirements that are necessary for this project- requirements are listed in `requirements.txt` within the root folder of the project. All the requirements are needed within this .txt file to properly run authorization flow and Artist model population.
- API secrets for Spotify are not included in the code. Implementation for the project was currently not possible in plaintext- the plan was to host on Heroku and store API secrets securely there, but it was not possible within the time of the last iteration. API secrets must be temporarily copied and pasted in the `CID` and `SECRET` variables within the `spauth(request)` function found in `spotify_auth/views.py`.
- To run the server and access the authorization flow, run the command `python manage.py runserver`, and access the locally hosted site at `http://localhost:8000/`.
- Click the "Log In With Spotify" button on the home page- it will prompt login with a legitimate Spotify account and authorize the Melody Madness application. The webpage will then redirect you to `/generate/`, which shall begin the process of generating the bracket.
- It is possible that Artists may appear in the bracket from previous users, due to the lack of multi-user login implementation. To fix this, one must login to the admin panel and remove artists within the artist model. 


### Testing
- Testing for Spotify authorization is not possible as the Spotify OAuth2 authorization flow is well documented and stable. In fact, testing this authorization is usually advised against.
- The tests for the `spotify_auth` app can be found under `spotify_auth/tests.py`.
- Testing largely consisted of Artist model population, alongside reading certain aspects of the Artist model and then deleting this model.
- There are also tests to confirm that Spotify's API is properly pulling 16 artists- but this requires API secrets mentioned above, and must be copied and pasted in similarly to the process used for `spauth(request)`. Without this process, the test will fail.
- Running the test suite for all tests is simple, by executing the command `python manage.py test`.

### Functionality
- The functionality of authorization is largely dependent on whether the Spotify API secrets can be provided to it. Obviously, implementation of these API secrets in plaintext is dangerous- but it was necessary as we needed to work on other functionality of the bracket. I also explicitly warned any other team members to ensure that they remove their keys before committing!
- If hosting of these secrets were properly set up via Heroku or another service such as GitHub Secrets, the authorization functionality would be perfectly stable.
- Additionally, there is currently no way to delete Artist objects after they have been populated. This is largely due to us not having enough time during the iterations to implement multi-user functionality. 