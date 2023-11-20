<template>
  <!-- Only render the app-header if showHeader is true -->
  <header v-if="showHeader" class="app-header">
    <div>
      <nav v-if="showLoginLink">
        <ul>
          <li class="centered">
            <RouterLink to="/home">Logout</RouterLink>
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
