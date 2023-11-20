<template>
  <header class="app-header">
    <div>
      <h1>{{ title }}</h1>
      <nav>
        <ul>
          <li>
            <RouterLink to="/studentcs">Browse Courses</RouterLink>
          </li>
        </ul>
      </nav>
      <div>
        <h2>Enrolled Courses:</h2>
        <ul>
          <li v-for="course in courses" :key="course.S">{{ course.S }}</li>
        </ul>

      </div>
    </div>
  </header>
</template>
  
<script setup>
import { onMounted, ref } from "vue";
import { RouterLink } from "vue-router";

// Define the reactive variables
const title = defineProps({
  title: {
    type: String,
    required: true,
  },
});

const courses = ref([]); // This will hold the list of courses
const username = ref(''); // You should have some logic to populate this with the current user's ID

// Function to fetch courses from the API
function listCourses() {
  let userId = username.value; // Make sure this is the actual UserID you need to send
  let endpoint = `https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/studenthomepage/enrollment?UserID=${userId}`;

  fetch(endpoint)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    // If the Lambda function returns the body as a stringified JSON, you should parse it
    courses.value = JSON.parse(data.body); // Update the courses reactive property
    // If the Lambda function returns the body as an object, you can assign it directly
    // courses.value = data.body; 
  })
  .catch(error => {
    console.error('An error occurred:', error);
  });
}

// Call listCourses on component mount
onMounted(() => {
  // Assuming that username gets its value before this onMounted hook runs
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
  