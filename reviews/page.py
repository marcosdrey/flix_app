import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()

    if reviews:
        reviews_df = pd.json_normalize(reviews)
        st.write('Lista de Avaliações')
        AgGrid(pd.DataFrame(reviews_df), key='reviews_grid')
    else:
        st.warning('Nenhuma review foi encontrada.')

    st.title('Cadastrar nova review')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movies_names = {movie['title']: movie['id'] for movie in movies}

    selected_movie = st.selectbox(
        label='Filme',
        options=list(movies_names.keys())
    )

    stars = st.number_input(
        label="Estrelas",
        min_value=0,
        max_value=5,
        step=1
    )

    comment = st.text_area(label="Comentário")

    movie_id = movies_names[selected_movie]

    if st.button('Criar Review'):
        new_review = review_service.create_review(movie_id, stars, comment)
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar a review. Verifique os campos.')
