## Recommendation Systems using Python
This project explores the concepts and algorithms used to create accurate recommendation systems based on user preference: supervised machine learning for the music recommendation system and data analysis for the movie recommendation system. 

## Motivation
The goal of this project was to combine my skills in computer/data science with interests and hobbies of mine (ex. watching movies and listening to music). Keep in mind, for the song recommendation program to work well, make sure to have two Spotify playlists of at least seventy songs in each of them (one playlist with songs you like and one with songs you dislike).

## Installation
Run this command in your terminal: 
```
git clone https://github.com/CharlesShi12/RecommendationSystems.git
```
Import the folder into your respected IDE. 
Install the necessary libraries/frameworks:
* Streamlit
* Sklearn
* Spotipy
* Pandas

Open your terminal, navigate to this github repository folder and run the following command:
```
streamlit run main.py
```

## General Technical Description
#### Music Recommendation System: 
This recommendation system builds on a machine learning classification model that is trained with user inputted data and can identify whether a song is liked or disliked based on the user's past preferences. Songs that users like are labeled as "1" and songs that users dislike are labeled as "0" in the 'favorite' column (also known as binary classification). Data gathering was done via spotipy. Data processing was done via pandas. Training and using machine learning classification models was done via sklearn. The machine learning model I used in this project was a machine learning classification model called Support Vector Machines. Support Vector Machines usually work well with smaller datasets that have some features which is evident in our case. Essentially, this is a form of content-based filtering where the algorithm classifies whether a song is good or bad based on how similar it is to the user's inputted playlists of liked and disliked songs. 

#### Movie Recommendation System: 
This recommendation system builds on collaborative filtering and statistical analysis. Using two downloaded datasets from MovieLens, the algorithm will look for movies that have the most correlation based on user reviews. For example, if user A likes movies 1 and 2 and user B likes movies 1 and 3, then we can predict that user A will like movie 3 because of user A and user B's shared past preferences. This type of predicting becomes increasingly more accurate with bigger datasets. We can compute the correlation between movies using the Pearson Correlation Coefficient. Data gathering was done via MovieLens. Data processing was done via pandas. Data analysis was done also via pandas.

## Features
* Users can chose whether they want a song or movie recommendation system 
* Users can enter the URI of playlists they want to use
* Users can enter the movie titles they want to use
* Recommendation system outputs the suggested songs/movies in a user-friendly format

## Demonstration
As of July 2020, these are the recommendations I am getting from my recommendation system. However, these recommendations could be much different sometime later. For instance, the Global Top 50 playlist is constantly updated by Spotify so the Global Top 50 playlist I am using right now for the demonstration could be much different than the Global Top 50 playlist later on in the future. Just keep this in mind. 

For the music recommendation system, I will be using https://open.spotify.com/playlist/7glc712oqMnuatn8fN2Mti?si=6R05rroLTPCiW6r_nIGY0A for the playlist with songs I like and https://open.spotify.com/playlist/0yoXH0JfXkhqL8tAdM05WC?si=zE6cbftZSY2GMn9nL2mayw for the playlist with songs I dislike. The playlist I like primarily consists of hip-hop and electronic dance music (EDM) with some other music genres scattered throughout the playlist. The playlist I dislike consists of mostly country and rock. For the movie recommendation system, I used Inception (2010), Interstellar (2014), and Arrival (2016) as my most favorite movies. 

#### Video Demonstration:
A video showing the features of my recommendation system is linked here: https://drive.google.com/file/d/14UY9L_s3pepVoWZe3ngmfQiCNzEQUQdl/view?usp=sharing. The machine learning model's accuracy score for these two playlists was 82%. 

#### Testing Demonstration: 
I calculated the average accuracy score for my machine learning model using various combinations of inputted playlists. After training and testing my machine learning model, the final average accuracy score was around 86%. The accuracy score is calculated by (number of points classified correctly) / (total number of points in your test set). The full Google Sheets spreadsheet is linked here: https://docs.google.com/spreadsheets/d/1qKlvqCxxP1JYaF8HTBFM1zw1QECT4n2-pvl3dBN-w-o/edit?usp=sharing. 

## Future Improvements
#### Music Recommendation System: 
This type of recommendation system isn't the best for practicality. For instance, not that many people will have playlists with over seventy songs they dislike. It may very inconvenient for users. Therefore, I could use other alternative methods of recommending songs for people such as collaborative filtering, however, from a learning perspective, this project taught me a lot. 

#### Movie Recommendation System: 
Even though I only inputted sci-fi and action-adventure movies, I noticed there were a couple of comedy and romance movies that this movie recommendation system suggested for me. Sci-fi and action-adventure seem to be the opposite of comedy and romance, so I could perhaps add a function where I look at the genres of each movie and recommend movies that are closely related to sci-fi and action-adventure. This could be done by splitting the types of genres in the 'genres' column of my DataFrame and putting those genres in an array (ex. [‘Drama’, ‘Mystery’, ‘War’]). Then you could loop through each movie’s genres array and keep the sci-fi genres, action-adventure genres, and genres that are related to either sci-fi or action-adventure. I could also use other ways to build recommendation systems such as cosine similarity. 

Finally, I could find more accurate ways to test my recommendation systems and measure their performance. 

## License
MIT © Charles Shi
