<template>
  <!-- Only render the app-header if showHeader is true -->
  <header v-if="showHeader" class="app-header">
    <div>
      <nav v-if="showLoginLink">
        <ul>
          <li class="centered">
            <RouterLink to="/home">Logout</RouterLink>
            <RouterLink v-if="$route.path.startsWith('/studentcs/')" :to="`/studenthome?userId=${$route.params.user}`">Homepage</RouterLink>
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

// By default, show the link and the header
const showLoginLink = ref(true);
const showHeader = ref(true); // New variable to control the header visibility

watch(route, (newRoute) => {
  // Hide the header and link only if on the home page
  const isHomePage = newRoute.path === '/home';
  showLoginLink.value = !isHomePage;
  showHeader.value = !isHomePage; // Hide the entire header on the home page
});
</script>

<style>
/* give the header itself a background color, a border, and add some padding to the content */
.app-header {
  background-color: #007BFF; /* Blue background */
  border-bottom: 1px solid #e0e0e0;
  padding: 1rem;
  text-align: center;
}

/* Logout button styles */
.app-header a {
  color: #fff; /* White text */
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  transition: background-color 0.3s, color 0.3s;
}

/* Highlight color on hover */
.app-header a:hover {
  background-color: #FFC107; /* Highlight color (example: yellow) */
  color: #000; /* Text color on hover (example: black) */
}
</style>
