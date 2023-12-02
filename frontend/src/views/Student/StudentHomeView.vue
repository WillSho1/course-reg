<template>
  <template v-if="isAuthenticated">
    <header class="app-header">
      <div class="header-content">
        <h1>Welcome {{ user.nickname }}!</h1>
      </div>
      <div class="course-search">
        <RouterLink to="/studentcs">Course Search</RouterLink>
      </div>
      <div class="course-list">
        <h3>Below are your enrolled courses:</h3>
        <ul>
          <li v-for="course in courses" :key="course" class="course-item">
            {{ course }}
            <button @click="dropCourse(course)">Drop</button>
            <button @click="getCourseInfo(course)">Get Info</button>
          </li>
        </ul>
      </div>
    </header>
    <div class="banner-image">
        <img src="/uconn-banner.png" alt="UCONN Banner" />
      </div>
  </template>
</template>


  
<script setup>
import { useAuth0 } from '@auth0/auth0-vue';
import { ref, watch, nextTick } from "vue";
import { RouterLink, useRouter } from "vue-router";

const { isAuthenticated, user } = useAuth0();
const router = useRouter();
const courses = ref([]); // This will hold the list of courses

let userID = null;
let role = null;

watch(user, async (newUser) => {   
  if (newUser && newUser.nickname) { 
    userID = newUser;
    role = newUser['dev-75fp6aop37uung0c.us.auth0.com/Role'];
    await nextTick();
    await new Promise(resolve => setTimeout(resolve, 0));
    if (role != 'Student' || !isAuthenticated) {
        router.push('/not-authorized');
        return;
    }
    listCourses();
  }
}, { immediate: true });

// Function to fetch courses from the API
function listCourses() {
  if (userID && userID.nickname) {
    let endpoint = `https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/studenthomepage/enrollment?UserID=${userID.nickname}`;
    fetch(endpoint)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        if (data.statusCode == '200'){
        console.log(data.body);
        courses.value = data.body; // Assuming the Lambda function returns the data in the body attribute
        }
        else {
          console.log(data.body);
          window.alert(data.body);
        }
      })
      .catch(error => {
        console.error('An error occurred:', error);
      });
  }
}

async function dropCourse(courseId) {
  try {
    const response = await fetch(`https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/studenthomepage/enrollment`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        'course_id_section': courseId,
        'UserID': userID.nickname
      })
    });

    const data = await response.json();

    if (response.ok) {
      console.log(data);
      listCourses(); // Refresh the course list
      alert(JSON.stringify(data.body, null, 2));
    } else {
      alert(JSON.stringify(data.body, null, 2));
      throw new Error(data);
    }
  } catch (error) {
    console.error('Error dropping course:', error);
  }
  listCourses()
}

async function getCourseInfo(courseIdSection) {
  try {
    const response = await fetch(`https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/studenthomepage/enrollment/courseinfo?course-id-section=${courseIdSection}`, {
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
