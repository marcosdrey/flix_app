from datetime import datetime
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
        st.write('Lista de Filmes')
        movies_df = pd.json_normalize(movies).drop(
            columns=['actors', 'genres.id']
        ).rename(columns={'genres.name': 'genre'})
        AgGrid(pd.DataFrame(movies_df), key='movies_grid')
    else:
        st.warning('Nenhum filme encontrado.')

    genre_service = GenreService()
    all_genres = genre_service.get_genres()
    genres_names = {genre['name']: genre['id'] for genre in all_genres}

    actor_service = ActorService()
    all_actors = actor_service.get_actors()
    actors_names = {actor['name']: actor['id'] for actor in all_actors}

    st.title('Cadastrar novo filme')

    title = st.text_input('Título do Filme')
    selected_genre_name = st.selectbox(
        label='Gênero do filme',
        options=list(genres_names.keys())
    )
    selected_actors_names = st.multiselect(
        label='Atores/Atrizes do Filme',
        options=list(actors_names.keys())
    )
    release_date = st.date_input(
        label='Data de Lançamento',
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    resume = st.text_area(
        label='Sinopse do Filme',
        max_chars=400
    )

    selected_genre_id = genres_names[selected_genre_name]
    selected_actors_ids = [actors_names[name] for name in selected_actors_names]

    if st.button('Criar Filme'):
        new_movie = movie_service.create_movie(
            title=title,
            release_date=release_date,
            genre_id=selected_genre_id,
            actors_ids=selected_actors_ids,
            resume=resume
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o filme. Verifique os campos.')
