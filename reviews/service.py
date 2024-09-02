import streamlit as st
from reviews.repository import ReviewRepository


class ReviewService:

    def __init__(self):
        self.repository = ReviewRepository()

    def get_reviews(self):
        if 'reviews' in st.session_state:
            return st.session_state.reviews
        reviews = self.repository.get_reviews()
        st.session_state.reviews = reviews
        return reviews

    def create_review(self, movie_id, stars, comment):
        review = {
            'movie': movie_id,
            'stars': stars,
            'comment': comment
        }
        new_review = self.repository.create_review(review)
        st.session_state.reviews.append(new_review)
        return new_review
