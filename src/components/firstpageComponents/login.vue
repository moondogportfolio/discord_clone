<template lang="pug">
form(autocomplete="off")
  q-input(
    v-model="username"
    label="Username")
  q-input(
    v-model="password"
    :type="view_password ? 'password' : 'text'"
    label="Password"
    autocomplete="off")
    template(v-slot:append)
      q-icon.cursor-pointer(
        :name="view_password ? 'visibility_off' : 'visibility'"
        @click="view_password = !view_password"
      )
  q-btn(
    @click="submit"
    label="Submit")
</template>

<script>


export default {
  name: "Login",
  sockets: {
    SERVER_HEARTBEAT_ACK() {
      console.log('SERVER HEARTBEAT ACKED')
      this.heartbeat_payload += 1
      console.log(this.heartbeat_payload)
    },
    // SERVER_HELLO(payload) {
    //   var heartbeat_sender = payload_send => {
    //     console.log('EMITTED')
    //     this.$socket.client.emit('HEARTBEAT', payload_send)
    //   }
    //   console.log(this.heartbeat_payload)
    //   // heartbeat_sender(null)
    //   // this.$socket.client.emit('HEARTBEAT', 1)
    //   // setTimeout(heartbeat_sender, 1000, 1)
    //   setInterval(
    //     () => {this.$socket.client.emit('HEARTBEAT', this.heartbeat_payload) },
    //     payload.heartbeat_interval)
    // }
  },
  data() {
    return {
      view_password: true,
      username: 'test',
      password: 'test',
      heartbeat_payload: 122,
    };
  },
  methods: {
    submit() {
      /*
      Get token, then call login_success.
      */
      this.$api({
        method: 'post',
        url: '/token',
        data: `grant_type=&username=${this.username}&password=${this.password}&scope=&client_id=&client_secret=`,
        headers : {
        'Content-Type': 'application/x-www-form-urlencoded',
         }
      }).then((response)=>{
        console.log("INIT_DATA");
        console.log(response.data)    
        sessionStorage.setItem('jwt', response.data.access_token)
        this.$router.push('/')
      }).catch((error) => {
        null
      })
    },
  },
};
</script>

<style>
</style>