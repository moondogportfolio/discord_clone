<template lang="pug">
q-scroll-area.full-height
  div(@click="route_goto_me")
    server-icon-vue.q-mt-sm(server_name="Home" icon="face" color="grey")
  template(v-for="server in servers" :key="server._id")
    div(@click="route_goto_server(server._id)")
      server-icon-vue(:server_name="server.name" :server_id="server._id")
        server-menu-vue
  add-server
    template(v-slot:icon)
      server-icon-vue(server_name="CREATE SERVER" icon="settings" color="grey")
  div(@click="route_goto_discover")
    server-icon-vue(server_name="DISCOVER" icon="people" color="grey")
  join-server-vue
    template(v-slot:icon)
      server-icon-vue(server_name="Join Server" icon="settings" color="grey")
</template>

<script>
import AddServer from "./addServer.vue";
import joinServerVue from './joinServer.vue';
import serverIconVue from "./serverIcon.vue";
import serverMenuVue from './serverMenu.vue';

export default {
  components: {
    serverIconVue,
    AddServer,
    serverMenuVue,
    joinServerVue
  },
  name: "ServerContainer",
  methods: {
    route_goto_me() {
      console.log('CHANGE ROUTE')
      this.$router.push('/channels/@me');
    },
    route_goto_discover() {
      this.$router.push('/channels/server-discovery');
    },
    async route_goto_server(id) {
      console.log('ENTER')
      var selected_server = null
      var selected_room = null
      await this.$api({
        method: 'put',
        url: `/server/${id}/enter`,
        headers : {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${this.$store.state.auth}`
         }
      }).then((response)=>{
        selected_server = response.data.serverdata.selected_serverdata._id
        selected_room = Object.entries(response.data.roomdata)[0]
        let userdata_update = {
          focused_room: selected_room[0],
          selected_room: selected_room[0],
          userdata: {
            state: {
              selected_room: selected_room[0],
              selected_channel: selected_room[1].channel,
              selected_server: selected_server,
              selected_view: 'server'
            }
          }
        }
        this.$store.commit('mutate_deep', userdata_update)
        this.$store.commit('mutate_deep', {roomdata: response.data.roomdata})
        delete response.data.roomdata
        this.$store.commit('mutate_shallow', response.data)
        this.$router.push(`/channels/${selected_server}/${selected_room[0]}`);
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  computed: {
    servers() {
      return this.$store.state.serverlist;
    },
  },
};
</script>

<style></style>

