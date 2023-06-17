<template lang="pug">
div.q-pa-md
	template(v-for="workspace in workspacelist" :key="workspace._id")
		q-item(clickable @click="view_workspace(workspace._id)")
			q-item-label {{ workspace.name }}
</template>

<script>
import { mapGetters, mapState } from 'vuex'


export default {
  computed: {
    ...mapState(['workspacelist']),
		...mapGetters(['userstate'])
  },
	methods: {
		view_workspace(workspace_id) {
			this.$store.commit('mutate_shallow', {selected_workspace: workspace_id})
		}
	}

}
</script>

<style>

</style>