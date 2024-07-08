// src/store.js
import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state: {
    rating: 0,
    submitted: false
  },
  mutations: {
    setRating(state, rating) {
      state.rating = rating;
    },
    setSubmitted(state, submitted) {
      state.submitted = submitted;
    },
    resetForm(state) {
      state.rating = '';
      state.submitted = false;
    }
  },
  actions: {
    async submitFeedback({ commit, state }) {
      try {
        const response = await axios.post('http://127.0.0.1:8000/feedback/', {
          rating: state.rating
        });
        console.log('Response:', response.data);
        commit('setSubmitted', true);
      } catch (error) {
        console.error('Error submitting feedback:', error);
      }
    }
  }
});

export default store;
