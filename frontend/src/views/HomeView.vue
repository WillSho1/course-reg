<template>
  <header class="home-header">
    <div id="root"></div>
    <div>
      <h1>{{ "Section 1 Group 7 Course System" }}</h1>
    </div>
  </header>
  <main class="home">
    <div class="login-section">
      <h2>Welcome to the Course Portal</h2>

      <!-- Auth0 login and signup buttons -->
      <div>
        <loginButton/>
        <!--<button @click="loginWithRole('Admin')">Login/Signup as Admin</button>
        <button @click="loginWithRole('Teacher')">Login/Signup as Teacher</button>-->
      </div>
    </div>

    <!-- For Login Failures
    <div class="modal" v-if="showModal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <p>{{ errorMessage }}</p>
      </div>
    </div>-->
  </main>
</template>

<script setup>
import loginButton from '../components/buttons/login-button.vue';
import { useAuth0 } from '@auth0/auth0-vue';

//const { isAuthenticated } = useAuth0();

</script>


<style>
.home {
  display: flex;
  align-items: flex-start; /* Align to the top of the container */
  justify-content: center;
  height: 100vh;
  padding: 1rem;
  
  /* Background image */
  background-image: url('/UConnImage.jpeg');
  background-size: cover;
  background-position: center center;
  background-repeat: no-repeat;
}

.login-section {
  text-align: center;
  padding: 1rem;
  padding-top: 5%; /* You can adjust this value to your preference */
}

.login-section h2 {
  font-size: 2.5rem; 
  margin-bottom: 1.5rem;
}

.credentials {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2rem;
}

.credentials input {
  padding: 0.5rem;
  border: 1px solid #d9d9d9;
  border-radius: 0.375rem;
}

.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  width: auto;
  max-width: 80%;
  
  padding: 10px;

  border: 2px solid #ff0000;
  border-radius: 5px;
  background: #fff;

  text-align: center;
}

.modal-content {
  position: relative;
}

.close {
  position: absolute;
  top: -70%; 
  right: -2.5%;
}

button {
  cursor: pointer;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.375rem;
  background-color: #007BFF;
  color: white;
  font-size: 1rem;
  margin: 0.5rem;
}

button:hover {
  background-color: #0056b3;
}


.home-header {
  background-color: #007BFF;
  border-bottom: 1px solid #e0e0e0;
  padding: 1rem;
  text-align: center;
}

.home-header h1 {
  font-size: 2rem;
  font-weight: bold;
}


</style>