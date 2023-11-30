<!--this is from the example in lab9-->

<template>
    <button class="button__login" @click="handleLogin">Log In</button>
  </template>
  
  <script setup>
  import { useAuth0 } from "@auth0/auth0-vue";
  
  const { loginWithRedirect } = useAuth0();
  
  const handleLogin = () => {
    loginWithRedirect({
      appState: {
        target: "/callback",
      },
    });
  };
  </script>