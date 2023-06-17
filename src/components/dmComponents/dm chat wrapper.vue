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
import chatContainer from '../chatComponents/single chat box.vue';
export default {
  name: 'chat_wrapper',
  components: { chatContainer },
  computed: {
    selected_thread() {
			return this.$store.state.userdata.state.selected_dm
    },
    post_entries() {
      return Object.entries(this.$store.state.roomdata[this.selected_thread].posts);
    },
  },
}
</script>

<style>

</style>