<template>
  <header class="app-header">
    <div>
      <h1>{{ title }}</h1>
      <nav v-if="showLoginLink">
        <ul>
          <li class="centered">
            <RouterLink to="/home">Go to login</RouterLink>
          </li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { RouterLink, useRoute } from "vue-router";
import { ref, watch } from 'vue';

const title = ref("Section 1 Group 7 Course System");
const route = useRoute();

// By default, show the link
const showLoginLink = ref(true);

watch(route, (newRoute) => {
  // Hide the link only if on the home page
  showLoginLink.value = newRoute.path !== '/home';
});
</script>

<style>
/* give the header itself a background color, a border, and add some padding to the content */
.app-header {
  background-color: #007BFF;
  border-bottom: 1px solid #e0e0e0;
  padding: 1rem;
  text-align: center;
}

/* make the title within the header a larger and bolder font */
.app-header h1 {
  font-size: 2rem;
  font-weight: bold;
}
</style>
