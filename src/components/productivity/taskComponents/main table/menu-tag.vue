<template lang="pug">
q-card
	q-card-section
		q-chip(
			v-for="option in selected_workspacedata?.field.tag.options"
			:key="option"
			clickable
			) {{ option }}
	q-card-actions
		q-input(v-model="new_tag" label="Add tag")
		q-btn(icon="add" unelevated @click="add_tag")
</template>

<script>
import { mapGetters } from 'vuex'

export default {
	data() {
		return {
			new_tag: null
		}
	},
	computed: {
		...mapGetters(['selected_workspacedata', 'userstate']),
	},
	methods: {
		add_tag() {
			let options_length = this.selected_workspacedata.field.tag.options?.length || 0
			console.log(`workspacedata.${this.userstate.selected_workspace}.field.tag.options.${[options_length]}`)
			this.$store.commit('mutate_set', {
				string: `workspacedata.${this.userstate.selected_workspace}.field.tag.options.${[options_length]}`,
				value: this.new_tag
			})
			this.new_tag = null;
		}
	}
}
</script>

<style>

</style>