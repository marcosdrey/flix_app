import requests
import streamlit as st
from login.service import logout


class ReviewRepository:

    def __init__(self):
        self.__base_url = 'https://devmarcosdrey.pythonanywhere.com/api/v1/'
        self.__reviews_url = f'{self.__base_url}reviews/'
        self.__headers = {
            'Authorization': f'Bearer {st.session_state.token}'
        }

    def get_reviews(self):
        response = requests.get(
            url=self.__reviews_url,
            headers=self.__headers
        )
        match response.status_code:
            case 200: return response.json()
            case 401:
                logout()
                return None
            case _: raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def create_review(self, review: dict):
        response = requests.post(
            url=self.__reviews_url,
            headers=self.__headers,
            data=review
        )
        match response.status_code:
            case 201: return response.json()
            case 401:
                logout()
                return None
            case _: raise Exception(f'Erro ao obter dados da API: {response.status_code}')
