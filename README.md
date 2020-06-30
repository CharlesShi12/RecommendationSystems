# Recommendation Systems using Python

# General Techincal Description
Music Recommendation System: 
This recommendation system builds on machine learning classification models that are trained with user inputted data and can indentify whether a song is liked or disliked based on the user's past preferences. Songs that users like are labeled as "1" and songs that users dislike are labeled as "0" in the 'favorite' column. Data gathering is done via Spotipy. Data processing is done via pandas. Choosing, training, and testing machine learning classification models are via sklearn. The machine learning models I used for this system are Support Vector Machines (more specifically, Support Vector Classifier), Naive Bayes Classifier, and K-Nearest Neighbors Classifier. 

Movie Recommendation System: 
This recommendation system builds on collaborative filtering and statistical analysis. Using two downloaded datasets from MovieLens, the algorithm will look for movies that have the most correlation based on user reviews. For instance, if user A likes movies 1 and 2 and user B likes movies 1 and 3, then we can predict that user A will like movie 3. This type of predicting becomes increasingly more accurate with more data. We can compute the correlations of movies via the Pearson Correlation Coefficient. Data gathering is done via MovieLens. Data processing is done via pandas. Data analysis is done also via pandas.

Ultimately, all the data, machine learning models, and algorithms within the music and movie recommendation systems are programmed into an interactive web application via streamlit. 

# Future Improvements
