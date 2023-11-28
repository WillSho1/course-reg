<template>
    <div>
      <header class="app-header">
        <div>
          <h1>{{ title }}</h1>
          <div>
            <h2>Enrolled Courses:</h2>
            <ul>
              <li v-for="course in courses" :key="course">{{ course }}</li>
            </ul>
          </div>
        </div>
      </header>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        title: "Teacher Homepage",
        courses: []
      };
    },
    mounted() {
      this.listCourses();
    },
    methods: {
      listCourses() {
        const userId = "YOUR_USER_ID"; // Replace with the actual user ID
        const endpoint = `https://YOUR_API_GATEWAY_URL/teacherhomepage/enrollment?UserID=${userId}`;
  
        fetch(endpoint)
          .then(response => {
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
          })
          .then(data => {
            this.courses = data; // Assuming the Lambda function returns an array of course IDs
          })
          .catch(error => {
            console.error('An error occurred:', error);
          });
      }
    }
  };
  </script>
  
  <style scoped>
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
  