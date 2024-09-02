import requests
import streamlit as st
from login.service import logout


class GenreRepository:

    def __init__(self):
        self.__base_url = 'https://devmarcosdrey.pythonanywhere.com/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_genres(self):
        response = requests.get(
            url=self.__genres_url,
            headers=self.__headers
        )
        match response.status_code:
            case 200: return response.json()
            case 401:
                logout()
                return None
            case _: raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def create_genre(self, genre: dict):
        response = requests.post(
            url=self.__genres_url,
            headers=self.__headers,
            data=genre
        )
        match response.status_code:
            case 201: return response.json()
            case 401:
                logout()
                return None
            case _: raise Exception(f'Erro ao obter dados da API: {response.status_code}')
