<template lang="pug">
div
  button(:id="server.name" @click="toggle") {{server.name}} 
  template( v-if="visibility")
    div.row 
      div(v-for="emoji in Object.entries(server.emoji)" :key="emoji")
        p {{emoji}}
        img.cursor-pointer.icon(
          :src="`http://localhost:8000/emojis/${server_id}/${emoji[0]}`"
          @mouseover=""
          @click="add_reaction(emoji[0])"
          )


</template>

<script>
export default {
  name: "EmoticonGroup",
  props: ["server"],
  computed: {
    server_id() {
      return this.$store.state.serverdata.selected_serverdata._id
    }
  },
  methods: {
    toggle() {
      this.visibility = !this.visibility;
    },
    hover(group, emoticon) {
      this.$store.commit("set_selected_emoticon", [group, emoticon]);
    },
    add_reaction(emoji_id) {
      let message_id = this.$store.state.selected_post
      let room_id = this.$store.state.roomdata.selected_roomdata._id
      this.$api({
        method: 'put',
        url: `/room/${room_id}/message/${message_id}/reaction/${emoji_id}/@me`,
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
         }
      }).then((response)=>{
      }).catch((error) => {
        console.log(error)
      })
      
    }
  },
  data() {
    return {
      visibility: true,
      src_folder: "dota_gif",
    };
  },

};
</script>

<style scoped>
.icon {
  height: 32px;
  width: 32px;
  margin: 4px;
}
</style>
