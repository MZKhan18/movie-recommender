import streamlit as st
import pickle
import pandas as pd
import requests

def fetchPoster(movie_id):
    response=  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e78c71df867e139df85e30f489ffc657&language=en-US%27'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = similarity[movie_index]
    movies_list = sorted(list(enumerate(dist)),reverse = True, key = lambda x: x[1])[1:6]
    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movie.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommended_movie_posters.append(fetchPoster(movie_id))
    return  recommended_movie, recommended_movie_posters

movies_dict = pickle.load(open('df_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)

similarity = pickle.load(open('simi.pkl','rb'))

st.title('Movie Recommender System')


selectedMovieName = st.selectbox(
    'Select a movie',
    movies['title'].values)

if st.button('Recommend'):
    names, poster  = recommend(selectedMovieName)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])
