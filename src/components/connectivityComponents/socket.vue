<template>
  <p style="display: none">===</p>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  name: "socket",
  computed: {
    socket() {
      return this.$socket.client;
    },
  },
  methods: {
    ...mapMutations([
      "mutate_shallow",
      "mutate_deep",
      "update_serverdata",
      "push_serverdata",
      "push_incoming_chat",
      "set_is_logged_in",


      "presence_update"
    ]),
  },
  sockets: {
    // connect(data) {
    //   console.log("socket connected");
    //   console.log(data);
    // },
    // presence_update(data) {
    //   this.presence_update(data)
    // },














    chat_sent(chat) {
      this.push_incoming_chat(chat);
    },
    server_credentials_sent(cred) {
      this.socket.auth.token = cred;
      this.socket.disconnect().connect();
      this.socket.emit('')
    },
    user_login(sid) {
      console.log("LOGIN DETECTED", sid);
    },
    user_disconnect(sid) {
      console.log("DISCONNECT", sid);
    },
    initial_data(initial_update) {
      console.log("INIT_DATA");
      this.set_is_logged_in()
      this.mutate_shallow(JSON.parse(initial_update));
    },
    server_join(userdata) {
      console.log("SERVER JOIN ", JSON.parse(userdata));
    },
    room_join(userdata) {
      console.log("ROOM JOIN ", JSON.parse(userdata));
    },
    update_data_shallow(shallow_update) {
      console.log("SHALLOW UPDATE");
      this.mutate_shallow(JSON.parse(shallow_update));
    },
    update_data_deep(deep_update) {
      console.log("DEEP UPDATE");
      console.log(JSON.parse(deep_update));
      this.mutate_deep(JSON.parse(deep_update));
    },
    push_data(push_update) {
      console.log("PUSH UPDATE");
      this.push_serverdata(JSON.parse(push_update));
    },
    server_list(val) {
      this.mutate_serverdata(val);
    },
  },
};
</script>

<style></style>
