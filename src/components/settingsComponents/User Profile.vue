<template lang="pug">
div.row
  div.col-6
    q-list( separator)
      q-item
        q-btn(icon="edit" color="deep-purple-12" unelevated) Change avatar
      q-item
        q-btn(icon="edit" color="deep-purple-12" unelevated) Change profile banner
      
      q-item
        q-item-section
          q-item-label About Me
          q-item-label(caption lines="1") Can be configured with markdown
          q-input.q-mt-md(filled v-model="about_me")
  div.col-6.q-pa-md
    member-details-vue.member-details
</template>

<script>
import memberDetailsVue from '../memberComponents/memberDetails.vue'

export default {
  components: {memberDetailsVue},
  data() {
    return {
      about_me: null
    }
  },
  computed: {
    userdata() {
      return this.$store.state.userdata
    }
  }
}
</script>

<style scoped>
.member-details {
  max-width:30vw;
}
</style>