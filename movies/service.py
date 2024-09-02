import streamlit as st
from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.repository = MovieRepository()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.repository.get_movies()
        st.session_state.movies = movies
        return movies

    def create_movie(self, title, genre_id, release_date, actors_ids, resume):
        movie = {
            'title': title,
            'genres': genre_id,
            'release_date': release_date,
            'actors': actors_ids,
            'resume': resume
        }
        new_movie = self.repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie

    def get_movie_stats(self):
        if 'movie_stats' in st.session_state:
            return st.session_state.movie_stats
        movie_stats = self.repository.get_movie_stats()
        st.session_state.movie_stats = movie_stats
        return movie_stats
