<template>
  <div class="loading-page">
    <p>Loading...</p>
  </div>
</template>

<script setup>
//post login page - used for redirection
import { useAuth0 } from '@auth0/auth0-vue';
import { watch, ref, nextTick } from 'vue';
import { useRouter } from 'vue-router';

//router, auth0
const router = useRouter();
const { user } = useAuth0();

//Auth0 information
let userID = ref('');
let role = '';

//watching for auth0 update - this is necessary to get user info and track authorization
watch(user,async (newUser) => {
    if (newUser && newUser.nickname) {
        //store info and Role metadata
        userID.value = newUser;
        role = newUser['dev-75fp6aop37uung0c.us.auth0.com/Role'];
        //waiting here as a bug fix - originally would have to refresh page for redirection to occur
        await nextTick();
        await new Promise(resolve => setTimeout(resolve, 0));
        //Redirect based on the user's role
        if (role == 'Teacher') {
            router.push('/teacherhome');
        } else if (role == 'Student') {
            router.push('/studenthome');
        }
    }
}, { immediate: true });

</script>

<style>
/* Add your styles here */
.loading-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-size: 1.5rem;
}
</style>
