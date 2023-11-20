<template>
  <header class="app-header">
    <div>
      <h1>{{ title }}</h1>
      <nav>
        <ul>
          <li>
            <RouterLink to="/studentcs">Go to Course Search</RouterLink>
          </li>
        </ul>
      </nav>
      <div>
        <h2>Enrolled Courses:</h2>
        <ul>
          <li v-for="course in courses" :key="course">{{ course }}</li>
        </ul>
      </div>
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
  /* give the header itself a background color, a border, and add some padding to the content */
  .app-header {
    background-color: #fcfcfc;
    border-bottom: 1px solid #e0e0e0;
    padding: 1rem;
  }
  
  /* make the title within the header a larger and bolder font */
  .app-header h1 {
    font-size: 2rem;
    font-weight: bold;
  }
  </style>
  