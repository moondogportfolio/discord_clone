<template>
  <router-view />
</template>
<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'App',
  // computed: {
  //   socket() {
  //     return this.$socket.client;
  //   }
  // },
  // created() {
  //   let token = localStorage.getItem('jwt');
  //   if (token == null) {
  //     this.$router.push('login');
  //   }
  //   else {
  //     console.log(this.socket)
  //     this.socket.auth.token = token;
  //     this.socket.emit('get_initial_data')
      
  //   }
  // }
})
</script>
