<template>
  <main class="home">
      <div class="login-section">
          <h2>Welcome to the Course Portal</h2>

          <div class="credentials">
              <input type="text" placeholder="Username" v-model="username">
              <input type="password" placeholder="Password" v-model="password">
          </div>

          <div class="login-options">
              <button @click="loginAs('student')">Login as Student</button>
              <button @click="loginAs('admin')">Login as Admin</button>
              <button @click="loginAs('teacher')">Login as Teacher</button>
          </div>
      </div>
  </main>
</template>

<script setup>
import { ref } from "vue";

const username = ref("");
const password = ref("");

function loginAs(role) {
  if (role === 'student') {
      console.log('Logging in as student...');
  } else if (role === 'admin') {
      console.log('Logging in as admin...');
  } else if (role === 'teacher') {
      console.log('Logging in as teacher...');
  }
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
