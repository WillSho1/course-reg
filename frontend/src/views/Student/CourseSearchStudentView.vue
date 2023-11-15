<template>
  <div>
    <div v-for="(subject, index) in subjects" :key="index" class="subject-row">
      <div class="subject-title" @click="selectSubject(index)">
        {{ Object.keys(subject)[0] }} {{ selectedSubject === index ? '▲' : '▼' }}
      </div>
      <div v-if="selectedSubject === index" class="courses-list">
        <h4>Courses for {{ Object.keys(subject)[0] }}</h4>
        <ul>
          <template v-if="Object.values(subject)[0].length === 0">
            <li>None listed</li>
          </template>
          <template v-else>
            <li v-for="(course, courseIndex) in Object.values(subject)[0]" :key="courseIndex">
              {{ course.courseid }} - {{ course.name }}
              <!--add description and prereqs-->
            </li>
          </template>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedSubject: null,
      subjects: [],
    };
  },
  created() {
    // Call your API function here
    this.fetchDataFromApi();
  },
  methods: {
    fetchDataFromApi() {
    let endpoint;
  
    endpoint = 'https://74ym2fsc17.execute-api.us-east-1.amazonaws.com/ProjAPI/studenthomepage/search';
  
    fetch(endpoint, {
      method: 'GET',
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        if (data.statusCode == 200) {
          console.log(data.body)
          //console.log(data)
          this.subjects = data.body
        }
      })
    .catch(error => {
      console.error('An error has occurred: ', error);
    })
    },
    selectSubject(index) {
      this.selectedSubject = this.selectedSubject === index ? null : index;
    },
  },
};
</script>

<style scoped>
.subject-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 5px;
  border: 1px solid #ccc;
  margin-bottom: 5px;
  cursor: pointer;
}

.subject-title {
  flex-grow: 1;
}

.courses-list {
  margin-top: 10px;
}
</style>
