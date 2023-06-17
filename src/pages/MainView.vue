<template lang="pug">
router-view(name='test-container')
div(v-if='settings_overlay')
  component.settings-overlay.absolute.window-height.window-width(:is='selected_setting_component')

.row.window-height
  .col.row.bodycont.full-height
    
    //- .col-3.full-height.row
    //-   .col-3.q-pr-sm
    //-     server-container-vue
    //-   .col.channelcont
    //-     router-view(name='dm-container')
    //-     router-view(name='channel-container')
    //-     router-view(name='workspace-left')
    //-     router-view(name='discover-sidebar')
    .col.full-height.column.maincont(style="background: #F2F3F5")
      
      .col-shrink
        router-view(name='friend-header-container')
        router-view(name='header-container')
        router-view(name='workspace-top')
      .col
        .row.full-height
          .col.full-height
            router-view(name='workspace-main')
            router-view(name='chat-container')
            router-view(name='center-container')
            router-view(name='dm-chat-container')
            router-view(name='discover-main')
          .col-shrink(style='max-width: 20vw;')
            router-view(name='workspace-right')
            router-view(name='active-friends-container')
            template(v-if='isvisible_members')
              router-view(name='member-container')
            router-view(name='participants-container')
  .col-shrink.thread-container.column(style="min-width:300px" v-if="isvisible_thread")
    router-view(name='thread-container')
</template>

<script>
import { defineComponent } from 'vue'
import serverContainerVue from "src/components/serverComponents/serverContainer.vue";
import settingsContainerVue from "src/components/settingsComponents/settingsContainer.vue";
import serverSettingsContainerVue from "src/components/settings-ServerComponents/serverSettingsContainer.vue";


var settings_dict = {
  'user_settings': settingsContainerVue,
  'server_settings': serverSettingsContainerVue
}

export default defineComponent({
  name: "MainView",
  sockets: {
    DATA_UPDATE(update) {
      console.log(update)
      this.$store.commit('socket_updates', update);
    },
    INIT_DATA_SEND(update) {
      console.log(update)
    }
  },
  computed: {
    isvisible_thread() {
      return this.$store.state.isvisible_thread
    },
    settings_overlay() {
      return this.$store.state.settings_overlay
    },
    isvisible_members() {
      return this.$store.state.isvisible_members
    },
    selected_setting_component() {
      return this.settings[this.$store.state.settings_component];
    },

  },
  components: {
    serverContainerVue,
    settingsContainerVue
  },
  created() {
    this.settings = settings_dict
  },
});
</script>

<style lang="sass">
.settings-overlay
  background: white
  z-index: 2

.bodycont
  background-color: #E3E5E8
  border-radius: 10px

body
  overflow: hidden
  background: black

.maincont
  background-color: white
  border-radius: 10px

.border-test
  border: 1px solid black

.channelcont
  background-color: #F2F3F5
  border-radius: 30px 0 0 0

.thread-container
  border-radius: 8px 0 0 8px
  margin-left: 10px
  background: white
  position: relative

kbd
  background: linear-gradient(-225deg,#d5dbe4,#f8f8f8)
  border-radius: 4px
  box-shadow: inset 0 -2px 0 0 #cdcde6, inset 0 0 1px 1px #fff, 0 1px 2px 1px #1e235a66
  color: #616161
  display: inline-block
  font-size: .8em
  line-height: 1
  margin: 0 .2em
  padding: 2px 4px 4px
  white-space: nowrap

.row-gap
  gap: 5px

.orgcombo-org
  background: #333
  padding: 2px 5px
  border-radius: 5px 0 0 5px
  color: #d9d9d9
  font-size: 12px

.orgcombo-role
  background: #4d4d4d
  padding: 2px 5px
  color: white
  font-size: 12px
  border-radius: 0 5px 5px 0


.q-table__card 
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px

</style>
