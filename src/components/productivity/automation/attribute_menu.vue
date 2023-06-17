<template lang="pug">
q-menu(anchor="top end" self="top start" )
	q-item(clickable @click="$emit('set_object', 'created_task')") metadata
		q-menu(anchor="top end" self="top start" )
			q-item(clickable @click="$emit('set_attribute', 'creator')") creator
			q-item(clickable @click="$emit('set_attribute', 'created_date')") created date
	q-item(clickable @click="$emit('set_object', 'created_task')") field
		q-menu(anchor="top end" self="top start" )
			q-item(
				clickable
				v-for="field in computed_field"
				:key="field"
				@click="$emit('set_attribute', field)") {{ field }}
	q-item(clickable @click="$emit('set_object', 'created_task')") group
	q-item(clickable @click="$emit('set_object', 'created_task')") board
	q-item(clickable @click="$emit('set_object', 'created_task')") task
</template>

<script>
import { mapGetters } from 'vuex'
export default {
	computed: {
		...mapGetters(['selected_workspacedata']),
		computed_field() {
			let x = []
			Object.entries(this.selected_workspacedata.field).forEach(ele => {
				if(['number', 'text'].includes(ele[0])) {
					ele[1].forEach(inner_ele=> x.push(inner_ele.fieldname))
				}
				else {
					x.push(ele[0])
				}
			})
			console.log(x)
			return x
		}
	}
	
}
</script>

<style>

</style>