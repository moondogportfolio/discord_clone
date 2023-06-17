<template lang="pug">
hr
.row
	q-icon(name="filter" size="32px")
q-card.q-ma-sm
//- div {{ grouped_tasks }}
//- div {{ task }}
//- div {{ tasks }}

.row
	q-card.q-ma-sm(v-for="status in status_options" :key="status.name")
		q-card-section
			|	{{ status }}
		q-card-section
			q-item(
				v-for="task in grouped_tasks[status.name]"
				:key="task.name"
				@click="set_dialog_task(task)"
				clickable)
				| {{ task.tasktitle }}
		q-card-section
			q-btn.full-width(icon="add" unelevated) Add task
	//- q-card.q-ma-sm
	//- 	q-card-section 
	//- 		q-item Card Columns
	//- 		q-item(v-for="column in columns" :key="column.field")
	//- 			q-item-section
	//- 				//- q-checkbox
	//- 			q-item-section
	//- 				q-item-label {{ column.label }}



q-dialog(v-model="isvisible_taskdialog")
	q-card(style="width:400px")
		q-card-section
			q-item(v-for="property in Object.entries(task)" :key="property[0]")
				q-item-section.q-mr-sm {{ property[0] }}
				q-item-section {{ property[1] }}
</template>

<script>
export default {
	props: ["tasks", "field"],
	methods: {
		set_dialog_task(task) {
			this.task = task
			this.isvisible_taskdialog = true
		}
	},
	computed: {
		status_options() {
			return this.field.status.options
		},
		grouped_tasks() {
			return _.groupBy(this.tasks, 'status')
		}
	},
	data() {
		return {
			task: null,
			isvisible_taskdialog: false
		}
	}
}
</script>

<style>

</style>