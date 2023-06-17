<template>
  <form autocomplete="off">
    <q-input v-model="username" label="Username" autocomplete="off" />
    <q-input
      v-model="password"
      :type="view_password ? 'password' : 'text'"
      label="Password"
      autocomplete="off"
    >
      <template v-slot:append>
        <q-icon
          :name="view_password ? 'visibility_off' : 'visibility'"
          class="cursor-pointer"
          @click="view_password = !view_password"
        />
      </template>
    </q-input>
    <q-btn @click="submit" label="Submit"></q-btn>
  </form>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      view_password: true,
      username: null,
      password: null,
    };
  },
  sockets: {
    register_success() {
      console.log('OK')
    }
  },
  methods: {
    submit() {
      this.$socket.client.emit("account_register", {
        username: this.username,
        password: this.password,
      });
    },
  },
};
</script>

<style>
</style>