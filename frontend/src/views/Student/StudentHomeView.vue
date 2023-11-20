<template>
  <header class="app-header">
    <div class="header-content">
      <h1>{{ title }}</h1>
    </div>
    <div class="course-search">
      <RouterLink to="/studentcs">Course Search</RouterLink>
    </div>
    <div class="course-list">
      <h3>Below are your enrolled courses:</h3>
      <ul>
        <li v-for="course in courses" :key="course" class="course-item">{{ course }}</li>
      </ul>
    </div>
  </header>
</template>


  
<script setup>
import { computed, onMounted, ref } from "vue";
import { RouterLink, useRoute } from "vue-router";

const title = computed(() => `Welcome ${username.value}`);

const courses = ref([]); // This will hold the list of courses

const route = useRoute(); // Initialize the route here
const username = ref(route.query.userId); // Retrieve the passed username

// Function to fetch courses from the API
function listCourses() {
  let userId = username.value;
  let endpoint = `https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/studenthomepage/enrollment?UserID=${userId}`;

  console.log(endpoint);
  fetch(endpoint)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      console.log(data.body);
      courses.value = data.body; // Assuming the Lambda function returns the data in the body attribute
    })
    .catch(error => {
      console.error('An error occurred:', error);
    });
}

// Call listCourses when the component is mounted
onMounted(() => {
  listCourses();
});
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
  font-size: 2rem;
  font-weight: bold;
}

/* Course search styles */
.course-search {
  margin-top: 1rem;
  padding: 0 2rem;
}
.course-search a {
  color: #005792;
  text-decoration: none;
  font-weight: bold;
  background-color: #fff;
  padding: 0.5rem 1rem;
  border-radius: 5px;
}

/* Course list styles */
.course-list {
  margin-top: 1rem;
  padding: 0 2rem;
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

</style>
