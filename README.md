# Recommendation Systems using Python
This project explores the concepts and algorithms used to create accurate recommendation systems based on user preference: machine learning for the music recommendation system and data analysis for the movie recommendation system. The goal of this project was to combine my skills in computer/data science with interests or hobbies of mine (ex. watching movies and listening to music). Keep in mind, for the song recommendation program to work well, make sure to have two Spotify playlists of at least fifty songs (one playlist with songs you like and one with songs you dislike).

# General Techincal Description
Music Recommendation System: 
This recommendation system builds on a machine learning classification model that is trained with user inputted data and can identify whether a song is liked or disliked based on the user's past preferences. Songs that users like are labeled as "1" and songs that users dislike are labeled as "0" in the 'favorite' column (also known as binary representation). Data gathering is done via Spotipy. Data processing is done via pandas. Training and using machine learning classification models are done via sklearn. The machine learning model I used in this project was a machine learning classification model called Support Vector Machines. Support Vector Machines usually work well with smaller datasets that some features which is evident in our case. 

Movie Recommendation System: 
This recommendation system builds on collaborative filtering and statistical analysis. Using two downloaded datasets from MovieLens, the algorithm will look for movies that have the most correlation based on user reviews. For instance, if user A likes movies 1 and 2 and user B likes movies 1 and 3, then we can predict that user A will like movie 3. This type of predicting becomes increasingly more accurate with bigger datasets. We can compute the correlations of movies via the Pearson Correlation Coefficient. Data gathering is done via MovieLens. Data processing is done via pandas. Data analysis is done also via pandas.

Ultimately, all of the data, machine learning models, and algorithms within the music and movie recommendation systems were programmed into an interactive web application via streamlit. 

# Future Improvements
Music Recommendation System: 
This type of recommendation system isn't the best for practicality. For instance, not that many people will have playlists with over fifty songs they dislike. It may very inconvenient for users. Therefore, I could use other alternative methods of recommending songs for people such as collaborative filtering, however, from a learning perspective, this project taught me a lot. 

Movie Recommendation System: 
Even though I only inputted sci-fi and action-adventure movies, I noticed there were a couple of comedy and romance movies that this movie recommendation system suggested for me. Sci-fi and action-adventure seem to be the opposite of comedy and romance, so I could perhaps add a function where I look at the genres of each movie and recommend movies that are closely related to sci-fi and action-adventure. This could be done by splitting the types of genres in the 'genres' column of my DataFrame and putting those genres in an array (ex. [‘Drama’, ‘Mystery’, ‘War’]). Then you could loop through each movie’s genres array and keep the sci-fi genres, action-adventure genres, and genres that are related to either sci-fi or action-adventure. I could also use other ways to build recommendation systems such as cosine similarity. 
