import requests
import streamlit as st
from login.service import logout


class MovieRepository:

    def __init__(self):
        self.__base_url = 'https://devmarcosdrey.pythonanywhere.com/api/v1/'
        self.__movies_url = f'{self.__base_url}movies/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_movies(self):
        response = requests.get(
            url=self.__movies_url,
            headers=self.__headers
        )
        match response.status_code:
            case 200: return response.json()
            case 401:
                logout()
                return None
            case _: raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def create_movie(self, movie: dict):
        response = requests.post(
            url=self.__movies_url,
            headers=self.__headers,
            data=movie
        )
        match response.status_code:
            case 201: return response.json()
            case 401:
                logout()
                return None
            case _: raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def get_movie_stats(self):
        response = requests.get(
            url=f'{self.__movies_url}stats/',
            headers=self.__headers
        )
        match response.status_code:
            case 200: return response.json()
            case 401:
                logout()
                return None
            case _: raise Exception(f'Erro ao obter dados da API: {response.status_code}')
