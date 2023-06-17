<template lang="pug">
template(v-if="post_entries")
  chat-container(:post_entries="post_entries" input_type="server")
q-spinner-grid.absolute-center(
  v-else
  color="primary"
  size="2em"
  )
</template>

<script>
import chatContainer from './single chat box.vue';
export default {
  components: { chatContainer },
  computed: {
    post_entries() {
      return Object.entries(this.$store.state.roomdata.selected_roomdata.posts);
    },
  },
}
</script>

<style>

</style>