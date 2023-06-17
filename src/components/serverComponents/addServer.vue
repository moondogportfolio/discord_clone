<template lang="pug">
div(@click="dialog_toggle=true")
  slot(name="icon")
q-dialog(v-model="dialog_toggle")
  q-card
    q-card-section
      .text-h6 Create server
    q-input(v-model="server_name" flat)
    q-card-actions(align="right")
      q-btn(
        flat
        label="OK"
        color="primary"
        v-close-popup
        @click="create_server"
        )

</template>

<script>
export default {
  name: "AddServer",
  data() {
    return {
      dialog_toggle: false,
      server_name: null,
    };
  },
  methods: {
    create_server() {
      let server_init = {
        "name": this.server_name,
        "channels": [
          {
            "name": "Channel 1",
            "rooms": [
              {
                "name": "Room 1"
              }
            ]
          }
        ]
      }
      this.$api({
        method: 'post',
        url: '/server',
        data: server_init,
        headers : {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${this.$store.state.auth}`
         }
      }).then((response)=>{
        console.log("INIT_DATA");
        console.log(response.data)    
        this.$store.commit('switch_server', response.data)
        console.log('JOINED SERVER')
        console.log(this.$store.state)
      }).catch((error) => {
        null
      })
    },
    socket_join_server(name) {
      console.log(name);
      console.log(this.$store.state.serverdata);
      if (!this.$store.state.serverdata.map((ele) => ele.name).includes(name)) {
        this.$socket.client.emit("join_server", "Infinity");
      }
    },
  },
};
</script>

<style></style>
