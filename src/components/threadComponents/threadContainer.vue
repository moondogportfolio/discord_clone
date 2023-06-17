<template lang="pug">
thread-header.col-shrink
chat-container.col(v-if="thread_mode == 'thread'" :post_entries="post_entries" input_type="thread")
create-thread.col(v-else-if="thread_mode == 'create'")
q-spinner-grid.absolute-center(
  v-else-if="thread_mode == 'loading'"
  color="primary"
  size="2em"
  )
</template>

<script>
import ChatContainer from '../chatComponents/single chat box.vue'
import ThreadHeader from './threadHeader.vue'
import CreateThread from './createThread.vue'

export default {
  components: { ThreadHeader, CreateThread, ChatContainer},
  name: 'threadContainer',
  computed: {
    thread_mode() {
      return this.$store.state.thread_mode;
    },
    post_entries() {
      return Object.entries(this.$store.state.threaddata.selected_threaddata.posts);
    }
  }
}
</script>

<style>

</style>