<template>
  <main class="form">
    <h2>Please enter a course to search for (Example: CSE 1010)</h2>

    <form @submit.prevent="searchCourses" class="search-course">
      <label for="courseQuery">Search:</label>
      <input type="text" id="courseQuery" name="courseQuery" v-model="courseQuery" />
      <button type="submit">Search</button>
    </form>

    <ul>
      <li v-for="(course, index) in courses" :key="course.subject + course.courseid">
        {{ course.subject }} {{ course.courseid }}
        <button @click="enrollInCourse(index)">Enroll</button>
      </li>
      <li v-if="courses.length === 0">
        <p>No courses found!</p>
      </li>
    </ul>
  </main>
</template>
  
<script setup>
import { ref } from "vue";

const courseQuery = ref("");

const courses = ref([]);

function searchCourses() {
    // Placeholder for API call
    // For now, just simulate a course search
    // Later, you'll replace this with an actual API call to fetch courses based on courseQuery.value
    courses.value = [{
        subject: "CSE",
        courseid: "1010"
    }, {
        subject: "MATH",
        courseid: "1100"
    }];
    
    courseQuery.value = ""; // Clear the search input after searching
}

function enrollInCourse(index) {
    // Logic to enroll the user in the selected course
    // You might push this to a user's course list or make another API call to save the enrollment
    console.log(`Enrolling in ${courses.value[index].subject} ${courses.value[index].courseid}`);
    courses.value.splice(index, 1); // Remove course from list after enrolling
}

</script>

  
  <style>
  .form {
    padding: 1rem;
  }
  
  .form h2 {
    font-size: 1.5rem;
    margin-bottom: 2rem;
  }
  
  .form p {
    margin-bottom: 1rem;
  }
  
  /* flex layouts allow us to position elements next to each other that would otherwise have been on top of each other */
  .form ul {
    display: flex;
    gap: 1rem;
    flex-direction: column;
  }
  .form li {
    display: flex;
    gap: 0.5rem;
    align-items: center;
  }
  
  /* create some space beneath the create todo form */
  .form form {
    margin-bottom: 1rem;
  }
  
  /* set some default styling to buttons and inputs for borders, heights, and padding */
  .form :is(input, button) {
    line-height: 2rem;
    padding-inline: 0.5rem;
    border-radius: 0.375rem;
    border: 1px solid #d9d9d9;
    margin-left: 0.5rem;
    color: #202020;
  }
  </style>
  