<template v-if="isAuthenticated">
  <header class="app-header">
    <div class="header-content">
      <h1>Welcome {{ Name }}!</h1>
    </div>
    <div class="divider"></div>
    <div class="course-list">
      <h2>Below are your enrolled courses:</h2>
      <ul>
        <li v-for="course in courses" :key="course" class="course-item">
          <span class="course-name">{{ course }}</span>
          <div class="course-info" v-if="courseInfo[course]">
          <ul>
            <li v-if="courseInfo[course].Location">
              <h4>Location:</h4> {{ courseInfo[course].Location }}
            </li>
              <br />
              <li v-if="courseInfo[course].StudentList">
                <h4>Student List:</h4> {{ courseInfo[course].StudentList }}
              </li>
              <li v-if="courseInfo[course].Schedule">
                <br />
                <h4>Schedule:</h4>
                <ul>
                  <li v-for="(time, day) in courseInfo[course].Schedule" :key="day">
                    {{ day }}: {{ time }}
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </li>
      </ul>
    </div>
  </header>
  <div class="banner-image">
    <img src="/uconn-banner.png" alt="UCONN Banner" />
  </div>
</template>


<script setup>
import { useAuth0 } from '@auth0/auth0-vue';
import { ref, watch, nextTick } from "vue";
import {  useRouter } from "vue-router";

const { isAuthenticated, user } = useAuth0();
const router = useRouter();
const courses = ref([]);
const courseInfo = ref({});

let userID = '';
let role = null;
let Name = '';

watch(user, async (newUser) => {   
  if (newUser && newUser.nickname) { 
    userID = newUser;
    role = newUser['dev-75fp6aop37uung0c.us.auth0.com/Role'];
    Name = newUser['dev-75fp6aop37uung0c.us.auth0.com/full_name'];
    //waiting here as a bug fix - originally would have to refresh page to have auth0 information show

    await nextTick();
    await new Promise(resolve => setTimeout(resolve, 0));
    if (role != 'Teacher' || !isAuthenticated) {
        router.push('/not-authorized');
        return;
    }
    listCourses();
  }
}, { immediate: true });

function listCourses() {
  if (userID && userID.nickname) {
    let endpoint = `https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/teacherhomepage/enrollment?UserID=${userID.nickname}`;
    fetch(endpoint)
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        if (data.statusCode == '200') {
          courses.value = data.body;
          courses.value.forEach(course => {
            getCourseInfo(course);
          });
        }
        else {
          alert(data.body);
        }
      })
      .catch(error => {
        console.error('An error occurred:', error);
      });
  }
}

async function getCourseInfo(courseIdSection) {
  try {
    const response = await fetch(`https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/teacherhomepage/enrollment/courseinfo?course-id-section=${courseIdSection}`, {
      method: 'GET'
    });
    const data = await response.json();
    if (response.ok) {
      // Assign the data to courseInfo
      courseInfo.value[courseIdSection] = JSON.parse(data.body);

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

.header-content h1 {
  color: #fff;
  text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000
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

.course-info{
  margin-left: 50rem;
}

</style>