<template lang="pug">
.header-bar.row.justify-end
	span #WAWAWEEWA THREAD NAME
	q-icon.cursor-pointer(name="more_horiz" size="24px " @click="")
		q-menu
			q-list
				q-item(clickable) Leave Thread
				q-item(clickable) Notification
				q-item(clickable) Open Full View
				q-separator
				q-item(clickable) Archive Thread
				q-item(clickable) Auto-archive
					q-menu(anchor="top start" self="top end")
						q-list
							q-item(clickable) 1 Hr
							q-item(clickable) 24 Hrs
				q-item(clickable) Delete Thread
	q-icon.cursor-pointer(name="close" size="24px " @click="hide_thread")


</template>

<script>
export default {
  name: "HeaderContainer",
  computed: {
    pinned_posts() {
      return Object.entries(this.$store.state.roomdata.selected_roomdata.posts).filter(ele => ele[1].pinned == true);
    }
  },
  methods: {
    hide_thread() {
      this.$store.commit('mutate_shallow', {isvisible_thread: false})
    }
  }
};
</script>

<style scoped>
.header-bar {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
  height: 48px;
  padding: 12px 0;
}
</style>
