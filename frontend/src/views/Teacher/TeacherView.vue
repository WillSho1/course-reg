<template>
  <template v-if="isAuthenticated">
    <header class="app-header">
      <div class="header-content">
        <h1>Welcom {{ userID.nickname }}!</h1>
      </div>
      <div class="course-list">
        <h3>Below are the courses you are teaching this semester:</h3>
        <ul>
          <li v-for="course in courses" :key="course" class="course-item">
            {{ course }}
            <button @click="getCourseInfo(course)">Get Info</button>
          </li>
        </ul>
      </div>
    </header>
  </template>
</template>


  
<script setup>
import { computed, onMounted, ref, watch, nextTick } from "vue";
import { useRouter } from "vue-router";
import { useAuth0 } from '@auth0/auth0-vue';

const { isAuthenticated, user } = useAuth0();
const router = useRouter();
const courses = ref([]); // This will hold the list of courses

let userID = '';
let role = null;

watch(user, async (newUser) => {   
  if (newUser && newUser.nickname) { 
    userID = newUser;
    role = newUser['dev-75fp6aop37uung0c.us.auth0.com/Role'];
    await nextTick();
    await new Promise(resolve => setTimeout(resolve, 0));
    if (role != 'Teacher' || !isAuthenticated) {
        router.push('/not-authorized');
        return;
    }
    listCourses();
  }
}, { immediate: true });

// Function to fetch courses from the API
function listCourses() {
  let endpoint = `https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/teacherhomepage/enrollment?UserID=${userID.nickname}`;

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

async function getCourseInfo(courseIdSection) {
  try {
    const response = await fetch(`https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/teacherhomepage/enrollment/courseinfo?course-id-section=${courseIdSection}`, {
      method: 'GET'
    });

    const data = await response.json();

    if (response.ok) {
      console.log(data.body);
      alert(JSON.stringify(data.body, null, 2)); // Display course info in a simple alert for now
    } else {
      throw new Error(data);
    }
  } catch (error) {
    console.error('Error fetching course info:', error);
  }
}

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