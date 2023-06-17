<template lang="pug">
.header-bar.row
  q-icon.cursor-pointer(name="push_pin" size="24px ")
    q-menu
      q-card
        q-card-section.text-bold.bg-grey-4
          div Pinned Messages
        q-list(bordered)
          q-item(v-for="post in pinned_posts" :key="post[0]")
            div.chat-single
              div
                q-avatar(size="42px")
                  img(src="~/assets/new_logo.jpg")
              div.q-mx-md(style="width: 100%")
                //- div.cursor-pointer.text-grey(v-if="reference") reply to: 
                  //- span.reference-content(@click="scroll_to_reference") {{ reference.content }} {{ post.message_reference }}
                div
                  div
                    span.text-bold.q-mr-sm {{ post[1].author }}
                    span {{ post[1].timestamp }}
                  div.text-bold post_id: {{post[0]}}
                  div {{ post[1].content }} 
  q-icon.cursor-pointer(name="group" size="24px " @click="toggle_member_visibility")
  q-icon.cursor-pointer#grid-items-sel(name="grid_view" size="24px ")
    grid-view-menu
  q-icon.cursor-pointer(name="check_box" size="24px " @click="create_todo")
  q-tabs.text-grey(v-model='server_header_tab', dense='', active-color='primary', indicator-color='primary', align='justify', narrow-indicator='')
    q-tab(name='mails', label='Overview')
    q-tab(name='alarms', label='Alarms')
    q-tab(name='movies', label='Movies')


todo-modal(:serverdata="selected_serverdata")
</template>

<script>
import { mapFields } from 'vuex-map-fields';
import GridViewMenu from './grid view menu.vue';
import todoModal from '../productivity/taskComponents/todo modal.vue'
import { mapGetters } from 'vuex';


export default {
  name: "HeaderContainer",
  components: {
    GridViewMenu, todoModal
    },
  computed: {
    ...mapFields(['server_header_tab']),
    ...mapGetters(['selected_serverdata']),
    pinned_posts() {
      return Object.entries(this.$store.state.roomdata.selected_roomdata.posts).filter(ele => ele[1].pinned == true);
    }
  },
  methods: {
    toggle_member_visibility() {
      let visibility = this.$store.state.isvisible_members
      this.$store.commit('mutate_shallow', {isvisible_members: !visibility})
    },
    create_todo() {
      this.$store.commit('mutate_shallow', {isvisible_todomodal: true})
    }
  },
  
};
</script>

<style scoped>
.header-bar {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
  height: 48px;
  padding: 12px 0;
}
</style>
