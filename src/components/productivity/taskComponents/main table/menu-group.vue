<template lang="pug">
q-card
	q-card-section
		q-chip(
			v-for="group in selected_workspacedata.field?.group.options"
			:key="group"
			clickable
			@click="set_attribute(group)"
			) {{ group }}
	q-card-actions
		q-input(v-model="new_group" label="Add group")
		q-btn(icon="add" unelevated @click="add_group")
</template>

<script>
import { mapGetters } from 'vuex'

export default {
	props: ["board_id", "task_id", "workspace_id"],
	data() {
		return {
			new_group: null
		}
	},
	computed: {
		...mapGetters(['selected_workspacedata', 'userstate']),
	},
	methods: {
		set_attribute(value) {
			var index = this.selected_workspacedata.board[this.board_id].task[this.task_id].group.indexOf(value)
			if(index==-1) {
				this.$store.commit('mutate_task', {
					workspace_id: this.workspace_id,
					board_id: this.board_id,
					task_id: this.task_id,
					attr: 'group',
					operation: 'push',
					value: value
				})
			}
			else {
				this.$store.commit('mutate_task', {
					workspace_id: this.workspace_id,
					board_id: this.board_id,
					task_id: this.task_id,
					attr: 'group',
					operation: 'splice',
					index: index
				})
			}
		},
		add_group() {
			var index = this.selected_workspacedata.field.group.options.indexOf(this.new_group)
			if(index==-1) {
				this.$store.commit('mutate_field', {
					workspace_id: this.workspace_id,
					field: 'group',
					attr: 'options',
					operation: 'push',
					value: this.new_group
				})
				this.new_group = null;
			}
			else {
				this.$store.commit('mutate_field', {
					workspace_id: this.workspace_id,
					field: 'group',
					attr: 'options',
					operation: 'splice',
					index: index
				})
				this.new_group = null;
			}
		}
	}
}
</script>

<style>

</style>