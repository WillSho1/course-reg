<template>
  <main class="home">
      <div class="login-section">
          <h2>Welcome to the Course Portal</h2>

          <div class="credentials">
              <input type="text" placeholder="Username" v-model="username">
              <input type="password" placeholder="Password" v-model="password">
          </div>

          <div class="login-options">
              <button @click="loginAs('Student')">Login as Student</button>
              <button @click="loginAs('Admin')">Login as Admin</button>
              <button @click="loginAs('Teacher')">Login as Teacher</button>
          </div>
      </div>
      <!-- For Login Failures -->
      <div class="modal" v-if="showModal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <!--<h3>Login Failed</h3>-->
        <p>{{ errorMessage }}</p>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from "vue";

const username = ref("");
const password = ref("");

function loginAs(role) {
  let endpoint;

  endpoint = 'https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/login';

  //make API request with following information
  fetch(endpoint, {
    method: 'POST',
    body: JSON.stringify({
      "UserID": username.value,
      "Type": role,
      "Password": password.value
    }),
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(response => {
      return response.json();
    })
    .then(data => {
      if (data.statusCode === 200) {
        // Successful login, display or process the API response data
        console.log(data.body);

        // Handle redirection based on the role in the Lambda response
        if (role == 'Student') {
          window.location.href = '/studenthome'; //redirect
        } else if (role == 'Teacher') {
          window.location.href = '/teacherhome';
        } else if (role == 'Admin') {
          window.location.href = '/adminhome';
        }
      } else {
        // Handle login failure
        //console.log(`Failed to log in as ${username.value}`);
        console.log(data.body); // You can display any error message or details from the Lambda function here.
        openModal(data.body);
      }
    })
    .catch(error => {
      console.error('An error occurred:', error);
    });
}

//functions for login failure
const showModal = ref(false);
const errorMessage = ref("");

function openModal(message) {
  errorMessage.value = message;
  showModal.value = true;
}

function closeModal() {
  showModal.value = false;
}

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
</style>
