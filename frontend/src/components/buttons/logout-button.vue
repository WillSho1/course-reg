<!--this is copied from the lab9 Auth0 example-->

<template>
    <button class="button__logout" @click="handleLogout">Log Out</button>
  </template>
  
  <script setup>
  import { useAuth0 } from "@auth0/auth0-vue";
  
  const { logout } = useAuth0();
  
  const handleLogout = () =>
    logout({
      logoutParams: {
        returnTo: window.location.origin,
      }
    });
  </script>

<style>
.button__logout {
  background-color: #000000; 
  color: white; 
  padding: 15px 32px; 
  text-align: center; 
  text-decoration: none; 
  display: inline-block;
  font-size: 16px; 
  margin: 4px;
  cursor: pointer; 
  border: none; 
  border-radius: 10px; 
}

.button__logout:hover {
  background-color: #007BFF;
}
</style>