import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actor_service = ActorService()
    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Atores/Atrizes')
        actors_df = pd.json_normalize(actors)

        AgGrid(actors_df, key='actors_grid')

    else:
        st.warning('Nenhum Ator/Atriz encontrado(a).')

    st.title('Cadastrar novo(a) Ator/Atriz')
    name = st.text_input('Nome do(a) ator/atriz')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['BRAZIL', 'USA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown
    )

    if st.button('Confirmar'):
        new_actor = actor_service.create_actor(name, birthday, nationality)
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o(a) ator/atriz. Verifique os campos novamente.')
