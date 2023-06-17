<template lang="pug">
q-item-section(top avatar)
  q-avatar
    img(src="~/assets/new_logo.jpg")
    q-badge(floating :color="member.connection == 'online' ? 'green': 'red'" rounded)
q-item-section
  q-item-label(
    lines="1"
  ) {{ member.nick }} aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaitem
  q-item-label.text-caption(
    lines="1"
  ) {{ member.nick }} aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaitem
q-menu.member-detail(
  width="30vw"
  height="100vh"
  anchor="top left"
  self="top right"
  )
  member-details-vue(style="max-width:30vw")
q-menu.q-pa-sm(context-menu
  anchor="top left"
  self="top right"
  )
  member-menu-vue
member-profile-vue
</template>

<script>
import memberDetailsVue from "./memberDetails.vue";
import memberMenuVue from './memberMenu.vue';
import memberProfileVue from './memberProfile.vue';

export default {
  name: "MemberSingle",
  props: ["member"],
  components: {
    memberProfileVue,
    memberDetailsVue,
    memberMenuVue
  },
};
</script>

<style></style>
