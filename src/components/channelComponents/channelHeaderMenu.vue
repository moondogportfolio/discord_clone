<template lang="pug">

q-menu.q-pa-sm(fit='' v-model="isvisible_menu")
  q-list
    q-item(clickable='' v-ripple='' @click="[isvisible_invite_modal, isvisible_menu]= [true, false]")
      q-item-section Invite people
      q-item-section(side)
        q-icon(name='settings' color="orange")
    q-item(clickable='' v-ripple='' @click="show_settings")
      q-item-section Server Settings
      q-item-section(side)
        q-icon(name='settings' color="green")
    q-item(clickable='' v-ripple='' @click="[isvisible_create_room_modal, isvisible_menu]= [true, false]")
      q-item-section Create room
      q-item-section(side)
        q-icon(name='settings' color="green")
      
    q-item(clickable='' v-ripple='' @click="[isvisible_create_channel_modal, isvisible_menu]= [true, false]")
      q-item-section Create channel
      q-item-section(side)
        q-icon(name='settings' color="green")
    q-separator
    q-item(clickable='' v-ripple='')
      q-item-section Notification settings
      q-item-section(side)
        q-icon(name='settings')
    q-item(clickable='' v-ripple='')
      q-item-section Privacy settings
      q-item-section(side)
        q-icon(name='settings')
    q-separator
    q-item(clickable='' v-ripple='')
      q-item-section Change Nickname
      q-item-section(side)
        q-icon(name='settings')
    q-item(clickable='' v-ripple='')
      q-item-section Hide Muted Channels
      q-item-section(side)
        q-icon(name='settings')
    q-separator
    q-item(clickable='' v-ripple='')
      q-item-section Leave Server
      q-item-section(side)
        q-icon(name='settings')

q-dialog(v-model="isvisible_invite_modal")
  q-card(style="min-width: 30vw")
    q-card-section
      p Invite friends to Mccndcg's server
    q-tabs(v-model="invite_tab")
      q-tab(label="Link" name="link")
      q-tab(label="Settings" name="settings")
    q-tab-panels(v-model="invite_tab")
      q-tab-panel(name="link")
        .text-caption Your link expires after {{invite_uses}} 
        q-input(outlined readonly v-model="server_invite_link")
          template(v-slot:append)
            q-btn(unleveled color="blue") Copy link
        q-card-actions
          q-btn(@click="create_invite" color="blue") Create Invite
          q-btn(@click="isvisible_invite_modal=false") Cancel
      q-tab-panel(name="settings")
        q-card-section
          q-select(outlined v-model="invite_expiration" :options="invite_options" label="Invite expiration")
        q-card-section
          q-input(outlined v-model="invite_max_uses" label="Max uses")
        q-card-section
          q-checkbox(v-model="invite_istemporary" label="Is temporary")
        q-card-actions
          q-btn(@click="create_invite" color="blue") Create Link
          q-btn(@click="isvisible_create_channel_modal=false") Cancel

q-dialog(v-model="isvisible_create_channel_modal")
  q-card.q-pa-sm
    q-card-section
      p.text-h6 Create Channel
    q-input(outlined v-model="new_channel_name" label="channel name")
    q-card-actions
      q-btn(@click="create_channel" color="blue") Create Channel
      q-btn(@click="isvisible_create_channel_modal=false") Cancel


q-dialog(v-model="isvisible_create_room_modal")
  q-card.q-pa-sm
    q-card-section
      p.text-h6 Create Room
    q-input(outlined v-model="new_room_name" label="name")
    q-input(outlined v-model="channel_name" label="channel name")
    q-select(outline v-model="channel_id" :options="server_channels" label="channel")
    q-card-actions
      q-btn(@click="create_room" color="blue") Create Room
      q-btn(@click="isvisible_create_room_modal=false") Cancel
        
</template>

<script>
export default {
  name: "ChannelHeaderMenu",
  computed: {
    server_channels() {
      return Object.keys(this.$store.state.serverdata.selected_serverdata.channels)
    }
  },
  data() {
    return {
      isvisible_create_channel_modal: false,
      isvisible_invite_modal: false,
      isvisible_create_room_modal: false,
      isvisible_menu: false,
      new_room_name: null,
      new_channel_name: null,
      channel_name: null,
      channel_id: null,

      server_invite_link: 'https://discord.gg/3h9ZeYZFM2',
      invite_tab: 'link',
      invite_expiration: null,
      invite_options: ['7 days', '1 day', '1 hour'],
      invite_max_uses: 0,
      invite_istemporary: false,
      invite_uses: '7 days'

    }
  },
  methods: {
    show_settings() {
      this.isvisible_menu = false;
      this.$store.commit('mutate_shallow', {settings_overlay: true});
    },
    create_invite() {
      let max_age = {
            days: 0,
            hours: 0,
            seconds: 0,
            weeks: 0
      }
      switch (this.invite_expiration) {
        case '7 days':
          max_age.days = 7;
          break;
        case '1 day':
          max_age.days = 1;
          break;
        case '1 hour':
          max_age.hours = 1;
          break;
      }
      this.$api({
        method: 'post',
        url: `/invite`,
        data: {
          server: this.$store.getters.server_id,
          room: this.$store.getters.room_id,
          inviter: this.$store.getters.user_id,
          max_uses: this.invite_max_uses,
          max_age: max_age,
          temporary: this.invite_istemporary
        },
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
        }
      }).then((response)=>{
          console.log(response);
          this.isvisible_invite_modal = false;
      }).catch((error) => {
          null
      })
    },
    create_room() {
      this.$api({
        method: 'post',
        url: `/server/${this.$store.state.serverdata.selected_serverdata._id}/rooms`,
        params: {
          name: this.new_room_name,
          channel_id: this.channel_id
        },
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
        }
      }).then((response)=>{
          console.log(response)
      }).catch((error) => {
          null
      })
      this.isvisible_create_room_modal = false;
      this.new_room_name = null;
      this.channel_name = null;
      this.channel_id =  null;
    },
    create_channel() {
      this.$api({
        method: 'post',
        url: `/server/${this.$store.state.serverdata.selected_serverdata._id}/channel`,
        params: {
          name: this.new_channel_name
        },
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
        }
      }).then((response)=>{
          console.log(response)
      }).catch((error) => {
          null
      })
      this.isvisible_create_channel_modal = false;
      this.new_channel_name = null;
    }
  }
};
</script>

<style></style>
