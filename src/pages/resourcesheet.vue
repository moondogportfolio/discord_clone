<template lang="pug">
//- div.shadow-1.q-ma-sm
//- 	q-card-section
//- 	q-card-section.q-my-sm
//- 		div.row.q-my-sm(v-for="item in 10" :key="item")
//- 			div.col-shrink
//- 				q-skeleton(type="QAvatar")
//- 			div.col 16

q-table.q-ma-lg(
	:rows="rows"
	:columns="columns"
	row-key="name"
	)
	template(v-slot:header="props")
		q-tr
			q-th(v-for="col in props.cols" :key="col.fieldname")
				| {{ col.label }}
	template(v-slot:top="props")
		div.row.full-width.position-relative
			div.col-shrink.text-h5.q-mr-sm Resourcesheet
			div.col.text-h5 Sep 12 - Sep 18, 2021
			div.col-shrink.absolute-right
				q-btn.q-ml-sm(icon="chevron_left")
				q-btn.q-ml-sm(icon="calendar_today")
				q-btn.q-ml-sm(icon="chevron_right")
	template(v-slot:bottom)
		q-btn SEND
	template(v-slot:body="props")
		q-tr
			q-td
				div.delivered(
					style="white-space: normal; text-align:center"
					)
					q-select(outlined dense)
					//- div
					//- 	|	{{ props.row.project }}
			q-td.delivered(
					style="white-space: normal; text-align:center"
					)
					q-select(outlined dense)
					//- div
					//- 	|	{{ props.row.task }}
			template(v-for="(col,index) in props.cols.slice(2)" :key="col.fieldname")
				q-td.table-cell(
					style="white-space: normal; text-align:center"
					)
					div
						|	{{ props.row?.[col.field] }}
					q-menu.round-border
						q-card-section.row
							q-input(label="Amount" outlined)
							q-input(label="Notes" outlined)
						q-card-section.position-relative
							span Add another entry
							q-btn.absolute-right.round-border Save


</template>

<script>
export default {
	data() {
		return {
			columns: [
				{name: 'project', label: 'Project', field: 'project'},
				{name: 'task', label: 'Task', field: 'task'},
				{name: 'sun', label: 'Sunday', field:'sun'},
				{name: 'mon', label: 'Monday', field:'mon'},
				{name: 'tue', label: 'Tuesday',field:'tue'},
				{name: 'total', label: 'Total',field:'total'},
				],
			rows: [
				{project: 'TEST PROJ', task: 'TASK', sun: 5, mon: 6, tue: 7, total: 8}
			]
		}
	}
}
</script>

<style>

.round-border {
	border-radius: 10px;
}
.delivered {
	border-left: 5px solid black;
}
</style>