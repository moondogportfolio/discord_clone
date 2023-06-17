<template lang="pug">

q-list
  q-item(clickable  @click="switch_route_friends")
    q-item-section(avatar)
      q-icon(name="people")
    q-item-section
      q-item-label Friends
  q-item(clickable @click="isvisible_add_friend_modal=true")
    q-item-section(avatar)
      q-icon(name="add")
    q-item-section
      q-item-label Add Friend
    
  q-separator
  q-item(clickable @click="isvisible_create_dm_modal=true")
    q-item-section(avatar)
      q-icon(name="add")
    q-item-section Create DM
      
  template(v-for="dm in roomdata" :key="dm.name")
    dm-section(:dm="dm" v-if="dm.type==2")

q-dialog(v-model="isvisible_add_friend_modal")
  q-card.q-pa-sm
    q-card-section
      .text-h6 Add Friend
    q-input(outlined v-model="friend_request_username" label="username")
      template(v-slot:append)
        q-btn(color="blue") Send Friend Request

q-dialog(v-model="isvisible_create_dm_modal")
  q-card.q-pa-sm
    q-card-section
      .text-h6 Create DM
    template(v-for="friend in friends" :key="friend")
      div
        span {{ friend_dict.[friend].username }}
        q-checkbox(v-model='form.id_array' :val="friend_dict.[friend]._id")
      q-input.q-py-sm.full-width(outlined v-model="form.name" label="name")
      q-btn.full-width(label="CREATE DM" @click="create_dm_room")


</template>

<script>
import { mapGetters, mapState } from 'vuex';
import DmSection from './friend panel dm section.vue'


export default {
  name: "FriendPanelFriends",
  components: { DmSection },
  methods: {
   
    switch_route_friends(){
      this.$router.push('/channels/@me')
    },
    add_friend() {
      this.$api({
        method: 'put',
        url: `/users/@me/relationships/${this.friend_request_username}`,
        headers : {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${this.$store.state.auth}`
         }
      }).then((response)=>{
        console.log("ADD_FRIEND");
      }).catch((error) => {
        console.error(error)
      })
      this.friend_request_username = null;
    },
    create_dm_room() {
      this.$api({
        method: 'post',
        url: '/dm_room',
        data: JSON.stringify({
          "participants": this.form.id_array.concat(this.userdata._id),
          "name": this.form.name
        }),
        headers : {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${this.$store.state.auth}`
         }
      }).then((response)=>{
        console.log("CREATE_CHANNEL_DM");
        // this.$store.commit('mutate_shallow',
        //   response.data.initial_data
        //   );
        // this.$router.push('friends')
        
      }).catch((error) => {
        console.error(error)
      })
      this.isvisible_create_dm_modal = false;
    }
  },
  data() {
    return {
      isvisible_add_friend_modal: false,
      isvisible_create_dm_modal: false,
      friend_request_username: null,
      form: {
        id_array: [], 
        name: null,
      }
    };
  },
  computed: {
    ...mapState(['roomdata', 'userdata']),
    ...mapGetters(['friend_dict', 'friends'])
  },
};
</script>

<style>
.dm-item:hover .q-item__section--side{
  visibility: visible;
}
.dm-item .q-item__section--side{
  visibility: hidden;
}
</style>