<template lang="pug">
div.q-pa-md
  template(v-for="type in relationship_types" :key="type")
    template(v-if="type[1].length > 0")
      div {{ translator[type[0]] }} -- {{ type[1].length }}
      template(v-for="friend in type[1]" :key="friend")
        q-item
          q-item-section(avatar)
            q-icon(name="settings" size="32px")
          q-item-section
            q-item-label {{ friend_dict[friend].username }}
            q-item-label(caption lines="1") {{ type[0] }}
          q-item-section(side v-if="['pending_incoming', 'pending_outgoing'].includes(type[0])")
            div
              q-icon.cursor-pointer(name="check_circle" size="32px" )
              q-icon.cursor-pointer(name="cancel" size="32px" v-if="type[0]=='pending_incoming'" @click="accept_friend")
        q-separator



</template>

<script>
import { mapGetters } from 'vuex';

export default {
  methods: {
    accept_friend() {
      this.$api({
        method: 'post',
        url: `/room/${this.selected_room}/message`,
        data: message,
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
         }
      }).then((response)=>{
        console.log(response)
      }).catch((error) => {
        null
      })
    }
  },
  computed: {
    ...mapGetters(['friend_dict']),
    translator() {
      return {'blocked': 'Blocked', 'friend': 'Friend', 'pending_incoming': 'Pending', 'pending_outgoing': 'Pending' }
    },
    relationship_types() {
      return Object.entries(this.$store.state.userdata.relationships)
      
    },
  },
};
</script>

<style>
</style>