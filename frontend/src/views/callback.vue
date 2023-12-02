<template>
  <div class="loading-page">
    <p>Loading...</p>
  </div>
</template>

<script setup>
import { useAuth0 } from '@auth0/auth0-vue';
import { watch, ref, nextTick } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const { user } = useAuth0();

let userID = ref('');
let role = '';

watch(user,async (newUser) => {
    if (newUser && newUser.nickname) {
        userID.value = newUser;
        role = newUser['dev-75fp6aop37uung0c.us.auth0.com/Role'];

        // Redirect based on the user's role
        await nextTick();
        await new Promise(resolve => setTimeout(resolve, 0));
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
