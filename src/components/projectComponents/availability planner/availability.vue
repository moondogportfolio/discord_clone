<template lang="pug">
general-table(
	:rows="rows"
	:columns="columns"
)
</template>

<script>
import { mapGetters } from 'vuex'
import generalTable from './table.vue'

export default {
	components: {
		generalTable
	},
	computed: {
		...mapGetters(['selected_workspacedata']),
		columns() {
			return [
				{name: 'start', label: 'Start', field: 'start'},
				{name: 'end', label: 'End', field: 'end'},
				{name: 'sun', label: 'Sunday', field:'sun'},
				{name: 'mon', label: 'Monday', field:'mon'},
				{name: 'tue', label: 'Tuesday',field:'tue'},
				{name: 'total', label: 'Total',field:'total'}
				]
		},
		rows() {
			return this.selected_workspacedata.member['61355552389a7e7a1d45dec7'].availability_rules
		}
	}
}
</script>

<style>

</style>