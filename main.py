# IMPORTS
import streamlit as st
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors
from sklearn.metrics import accuracy_score
import pandas as pd

# Prompt users to select whether they want a movie or track recommendation system
if (st.sidebar.checkbox("Check me for the Movie Recommendation System")):

    # User selects the checkbox to indicate that he or she wants the movie recommendation system
    st.title("MOVIE RECOMMENDATION SYSTEM")

    # User inputs three of their most favorite movies
    userInput1 = st.sidebar.text_input("Enter the First Movie You Like (ex. Matrix, The (1999)):")
    userInput2 = st.sidebar.text_input("Enter the Second Movie You Like:")
    userInput3 = st.sidebar.text_input("Enter the Third Movie You Like:")

    # User presses "Recommend Movies!" button
    if (st.sidebar.button("Recommend Movies!")):
        with st.spinner("Generating your Movies Recommendation List..."):
            try:
                # Read the datasets gathered from MovieLens
                titles = pd.read_csv("movies.csv")
                data = pd.read_csv("ratings.csv")

                # Data processing
                data = pd.merge(titles, data, on="movieId")
                reviews = data.groupby("title")["rating"].agg(["count", "mean"]).reset_index().round(1)
                movies = pd.crosstab(data["userId"], data["title"], values=data["rating"], aggfunc="sum")

                # Computing Pearson Correlation Coefficients to find the most similar movies to the user movies input
                similarity = movies.corrwith(movies[userInput1], method="pearson") + movies.corrwith(movies[userInput2],
                                             method="pearson") + movies.corrwith(movies[userInput3], method="pearson")
                correlatedMovies = pd.DataFrame(similarity, columns=["correlation"])
                correlatedMovies = pd.merge(correlatedMovies, reviews, on="title")
                correlatedMovies = pd.merge(correlatedMovies, titles, on="title")

                # Filtering certain movies to produce accurate recommendations
                output = correlatedMovies[(correlatedMovies["mean"] > 3.5) &
                                          (correlatedMovies["count"] >= 100)].sort_values("correlation",
                                                                                          ascending=False)
                output = output[
                    ((output.title != userInput1) & (output.title != userInput2) & (output.title != userInput3))]

                # Outputting the recommended movies in a user friendly format
                for index in range(0, 25):
                    st.markdown("")
                    st.markdown("#" + str(index + 1) + ". " + output.iloc[index]['title'])
                    st.markdown(output.iloc[index]["genres"])
                    st.markdown("")
            except:
                st.error("Uh oh, please try again! Your input format or movie release date may be incorrect.")

# User doesn't select the checkbox indicating that he or she wants the track recommendation system
else:

    # Acessing Spotipy (a Spotify Library) to gather our data from Spotify
    USERNAME = 'charles_shi12'
    SPOTIPY_CLIENT_ID = '80063f66798948fdba77036647d788d1'
    SPOTIPY_CLIENT_SECRET = 'b93e4d4ae5794eeb8e5b7a2104c2b745'
    REDIRECT_URI = 'http://localhost:8886/callback'
    SCOPE = 'playlist-read-private'
    token = util.prompt_for_user_token(USERNAME, SCOPE, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, REDIRECT_URI)
    credentials = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
    spty = spotipy.Spotify(client_credentials_manager=credentials)


    # METHODS
    # Collects a song's information
    def get_data(song):
        if ((song["track"] != None)):
            track_feature = {}
            # Track's metainformation
            information = spty.track(song["track"]["id"])
            # Track's features
            features = spty.audio_features(song["track"]["id"])
            for meta in ["id", "name"]:
                track_feature[meta] = song["track"][meta]
            for parameter in ["danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness",
                              "instrumentalness",
                              "liveness", "valence", "tempo"]:
                track_feature[parameter] = features[0][parameter]
            track_feature["artist"] = information["album"]["artists"][0]["name"]
            track_feature["popularity"] = information["popularity"]
            track_feature["album"] = information["album"]["name"]
            track_feature["url"] = information["album"]["images"][0]["url"]
            return track_feature
        else:
            return null


    # Creates a playlist DataFrame with liked songs (labeled as 1) and disliked songs (labeled as 0) in the "favorite" column
    def create_good_bad_playlist(goodPlaylist, badPlaylist):
        totalGood = spty.user_playlist_tracks("spotify", goodPlaylist)["items"]
        index = 0
        playlist_dataFrame = pd.DataFrame(
            columns=["id", "name", "artist", "popularity", "album", "url", "danceability", "energy", "key", "loudness",
                     "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo"])
        for song in totalGood:
            track_dataFrame = pd.DataFrame(get_data(song), index=[index])
            track_dataFrame["favorite"] = 1
            playlist_dataFrame = playlist_dataFrame.append(track_dataFrame)
            index += 1
        totalBad = spty.user_playlist_tracks("spotify", badPlaylist)["items"]
        for song in totalBad:
            track_dataFrame = pd.DataFrame(get_data(song), index=[index])
            track_dataFrame["favorite"] = 0
            playlist_dataFrame = playlist_dataFrame.append(track_dataFrame)
            index += 1
        playlist_dataFrame = playlist_dataFrame.dropna(axis=0)
        return playlist_dataFrame


    # Creates a regular playlist DataFrame with no "favorite" column
    def create_playlist(playlist):
        total = spty.user_playlist_tracks("spotify", playlist)["items"]
        index = 0
        playlist_dataFrame = pd.DataFrame(
            columns=["id", "name", "artist", "popularity", "album", "url", "danceability", "energy", "key", "loudness",
                     "mode", "speechiness", "acousticness", "instrumentalness", "liveness", "valence", "tempo"])
        for song in total:
            track_dataFrame = pd.DataFrame(get_data(song), index=[index])
            playlist_dataFrame = playlist_dataFrame.append(track_dataFrame)
            index += 1
        playlist_dataFrame = playlist_dataFrame.dropna(axis=0)
        return playlist_dataFrame


    # Returns an array of recommended songs using the most accurate machine learning classification model
    def song_recommendations(playlist):
        recommendations = []
        if (naive_score > SVM_score) and (naive_score > forest_score):
            method = GaussianNB()
            method.fit(x_train, y_train)
        elif (neighbors_score > SVM_score) and (neighbors_score > naive_score):
            method = neighbors.KNeighborsClassifier()
            method.fit(x_train, y_train)
        else:
            method = svm.SVC()
            method.fit(x_train, y_train)
        for index in range(0, len(playlist.index)):
            userInput = [playlist.iloc[index][6:].values]
            userInput = scaler.transform(userInput)
            output = method.predict(userInput)
            if (output == 1):
                recommendations.append(playlist.iloc[index][:6].values)
        return recommendations


    # Returns the URI of the user's selected playlist
    def func(input):
        return comparision[input]


    # Streamlit widgets combined with Python algorithms
    st.title("MUSIC RECOMMENDATION SYSTEM")
    if (st.sidebar.checkbox("Show me how to find Spotify's URI")):
        st.image("https://distrokid.zendesk.com/hc/article_attachments/360021233173/mceclip0.png")

    # User Inputs/Data Gathering
    goodplaylist = st.sidebar.text_input("Enter the URI of a Playlist You Like:")
    goodplaylist = goodplaylist[17:]
    badplaylist = st.sidebar.text_input("Enter the URL of a Playlist You Dislike:")
    badplaylist = badplaylist[17:]
    comparision = {"playlist": "Select a Playlist",
                   "spotify:playlist:6UeSakyzhiEt4NB3UAd6NQ": "Billboard Hot 100",
                   "spotify:playlist:37i9dQZEVXbMDoHDwVN2tF": "Global Top 50",
                   "spotify:playlist:37i9dQZEVXbLiRSasKsNU9": "Global Viral 50",
                   "spotify:playlist:37i9dQZEVXbKuaTI1Z1Afx": "United States Viral 50",
                   "spotify:playlist:37i9dQZF1DX1lVhptIYRda": "Hot Country",
                   "spotify:playlist:37i9dQZF1DX4WYpdgoIcn6": "Chill Hits",
                   "spotify:playlist:37i9dQZF1DX8tZsk68tuDw": "Dance Rising",
                   "spotify:playlist:37i9dQZF1DX2Nc3B70tvx0": "Ultimate Indie",
                   "spotify:playlist:37i9dQZF1DX83I5je4W4rP": "Beach Vibes",
                   "spotify:playlist:37i9dQZF1DWT5MrZnPU1zD": "Hip Hop Controller"}
    if (st.sidebar.checkbox("Do you want to use your own playlist? (Check the Box for Yes)")):
        option = st.sidebar.text_input('Enter the URI of Playlist You Want to Compare:')
    else:
        option = st.sidebar.selectbox("Select a Playlist for Our Algorithm to Search Through",
                                      options=list(comparision.keys()), format_func=func)
    option = option[17:]

    # User clicks the "Recommend Songs!" button
    if (st.sidebar.button("Recommend Songs!")):
        with st.spinner("Generating your Track Recommendation Playlist..."):
            # User doesn't chose a playlist leaving it on the default "Select a Playlist" option
            if (option == "playlist"):
                st.error("Please Choose a Playlist to Search Through")
            else:
                try:
                    playlist = create_good_bad_playlist(goodplaylist, badplaylist)
                    sorted_playlist = pd.DataFrame(playlist,
                                                   columns=["id", "name", "artist", "popularity", "album", "url",
                                                            "danceability", "energy", "key", "loudness",
                                                            "mode", "speechiness", "acousticness",
                                                            "instrumentalness",
                                                            "liveness", "valence", "tempo", "favorite"])

                    # Training algorithms based on the user's inputted playlists
                    x = sorted_playlist.drop(["id", "name", "artist", "popularity", "album", "url", "favorite"], axis=1)
                    y = sorted_playlist["favorite"]
                    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.15, random_state=100)
                    scaler = StandardScaler()
                    x_train = scaler.fit_transform(x_train)
                    x_test = scaler.transform(x_test)

                    # Support Vector Classification Model
                    support_vector = svm.SVC()
                    support_vector.fit(x_train, y_train)
                    vector_prediction = support_vector.predict(x_test)
                    SVM_score = accuracy_score(y_test, vector_prediction)

                    # Naive Bayes Classification Model
                    naive_bayes = GaussianNB()
                    naive_bayes.fit(x_train, y_train)
                    bayes_prediction = naive_bayes.predict(x_test)
                    naive_score = accuracy_score(y_test, bayes_prediction)

                    # K Nearest Neighbors Classification Model
                    nearest_neighbors = neighbors.KNeighborsClassifier()
                    nearest_neighbors.fit(x_train, y_train)
                    neighbors_prediction = nearest_neighbors.predict(x_test)
                    neighbors_score = accuracy_score(y_test, neighbors_prediction)

                    # Creating the recommended songs
                    compare = create_playlist(option)
                    sorted_compare = pd.DataFrame(compare,
                                                  columns=["id", "name", "artist", "popularity", "album", "url",
                                                           "danceability",
                                                           "energy", "key", "loudness", "mode", "speechiness",
                                                           "acousticness",
                                                           "instrumentalness", "liveness", "valence", "tempo"])
                    recommendations = song_recommendations(sorted_compare)

                    # Returns the recommended songs in a readable format
                    for i in recommendations:
                        st.markdown("")
                        st.markdown("**[" + i[1] + "]" + "(https://open.spotify.com/track/" + i[0] + ")**")
                        st.markdown("_" + i[2] + "_")
                        st.image(i[5], width=200)
                        st.markdown("")

                    # No songs were recommended from this playlist
                    if (len(recommendations) == 0):
                        st.error(
                            "Unfortunately, no songs were recommended from this playlist. Try again with different playlist!")
                except:
                    st.error("Sorry! Please try again or try with a different playlist.")
