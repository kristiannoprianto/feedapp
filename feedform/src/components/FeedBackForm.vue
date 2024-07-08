<template>
    <div class="star-rating-form">
      <h2>How would you rate your satisfaction with our product?</h2>
      <form @submit.prevent="submitForm">
        <div class="">
          <div class="stars">
            <span
              v-for="star in 5"
              :key="star"
              class="star"
              :class="{ 'filled': star <= rating }"
              @click="selectRating(star)"
            >
              ★
            </span>
          </div>
          <div class="rate-details">
            <p>
                Very dissatisfied
            </p>
            <p>
                Very satisfied
            </p>
          </div>
        </div>
        <button type="submit">Rate us!</button>
      </form>
      <!-- <p v-if="rating == 5">You rated us {{ rating }} stars. Thank you!</p>

      <p v-else>Please rate our service:</p> -->
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { computed } from 'vue';
  import { useStore } from 'vuex';
  
  export default {
    setup() {
      const store = useStore();
      const rating = computed(()=>store.state.rating)
  
      const selectRating = (selectedRating) => {
        store.commit('setRating', selectedRating)
      };

      const submitForm = async () => {
        await store.dispatch('submitFeedback');
      };
  
      return {
        rating,
        selectRating,
        submitForm
      };
    }
  };
  </script>
  
  <style scoped>
  .star-rating-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .stars {
    font-size: 24px;
  }
  
  .star {
    cursor: pointer;
    color: #ccc;
    transition: color 0.3s ease-in-out;
  }
  
  .star.filled {
    color: gold;
  }
  .rate-details{

  }
  </style>
  