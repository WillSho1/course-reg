<template>
    <template v-if="isAuthenticated">
        <header class="app-header">
            <div class="header-content">
            <h1>Welcome, {{ user.nickname }}!</h1>
            </div>
            <div class="course-list">
            <h3>Below are your enrolled courses:</h3>
            <ul>
            </ul>
            </div>
        </header>
        <div class="banner-image">
            <img src="/uconn-banner.png" alt="UCONN Banner" />
            </div>
    </template>
    <template v-else>
        Not Authorized
    </template>
</template>


<script setup>
import { useAuth0 } from '@auth0/auth0-vue';
const { isAuthenticated, user } = useAuth0();



</script>

<style>
/* General page styles */
body {
  font-family: 'Arial', sans-serif;
  color: #333;
  margin: 0;
  padding: 0;
}

/* Header styles */
.app-header {
  background-color: #005792;
  color: #fff;
  padding: 1rem 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 3rem;
  font-weight: bold;
}

/* Course search styles */
.course-search {
  margin-top: 2rem;
  padding: 0 2rem;
}
.course-search a {
  color: #005792;
  text-decoration: none;
  font-weight: bold;
  background-color: #fff;
  padding: 1rem 2rem;
  border-radius: 4px;
  font-size: 1.5rem;
}

/* Course list styles */
.course-list {
  margin-top: 2rem;
  padding: 0 .5rem;
}
.course-list h3 {
  color: white;
  font-size: 1.25rem;
  font-weight: bold;
}
.course-item {
  background-color: #e0e0e0;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  margin: 0.5rem 0;
}

.banner-image img {
  width: 100%; /* Set the width as needed */
  height: auto; /* Maintain aspect ratio */
  display: block; /* Remove any extra space below the image */
  margin: 1rem 0; /* Add some space around the image */
}

</style>
