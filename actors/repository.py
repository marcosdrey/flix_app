import requests
import streamlit as st
from login.service import logout


class ActorRepository:

    def __init__(self):
        self.__base_url = 'https://devmarcosdrey.pythonanywhere.com/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            url=self.__actors_url,
            headers=self.__headers
        )
        match response.status_code:
            case 200: return response.json()
            case 401:
                logout()
                return None
            case _: raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')

    def create_actor(self, actor):
        response = requests.post(
            url=self.__actors_url,
            headers=self.__headers,
            data=actor
        )
        match response.status_code:
            case 201: return response.json()
            case 401:
                logout()
                return None
            case _: raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
