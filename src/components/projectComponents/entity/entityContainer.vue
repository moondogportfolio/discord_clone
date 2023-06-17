<template lang="pug">
q-table.q-ma-sm.main-table(
	:rows="rows"
	:columns="columns"
	row-key="id"
	v-if="true"
	)
	//- template(v-slot:top)
	template(v-slot:header="props")
		q-tr
			q-th icon
			q-th(v-for="col in props.cols" :key="col.fieldname")
				| {{ col.label }}
				//- | {{ col.fieldname }}
				//- | {{ col.type }}
			//- q-th
			//- 	q-btn(icon="add_circle_outline" dense)
	template(v-slot:body="props")
		q-tr
			q-td
				q-skeleton(type="QAvatar" size="36px")
			template(v-for="col in props.cols" :key="col.fieldname")
				q-td.table-cell(
					style="white-space: normal; text-align:center"
					)
					template(v-if="col.fieldname=='entity'") 
						//- template(v-for="member in Object.entries(props.row[1]?.[col.fieldname])")
						//- 	div {{ member[0] }}
						//- 	div {{ member[1] }}
						div.row.row-gap(style="max-width: 300px;")
							q-skeleton(type="QAvatar" v-for="item in 16" :key="item" size="36px")
					template(v-else-if="col.fieldname=='task'") 
						div ✅ Finished: 12
						div ❌ Unfinished: 5
						div ⏳ Deadline Today: 2
						div 📅 Upcoming Tomorrow: 12
					template(v-else-if="col.fieldname=='relationship'")
						span.text-bold Joy Division
						span  --
						span Affiliate
					div(v-else) {{ props.row[1]?.[col.fieldname] }}
					q-menu.q-pa-sm(context-menu style="width: 350px;")
						member-menu(v-if="col.fieldname=='entity'")
		q-tr
			q-td(colspan="100%")
				q-item(v-for="item in 2" :key="item" clickable)
					q-item-section(avatar)
						q-skeleton(type="QAvatar")
					q-item-section
						q-item-label Name
					q-item-section(side)
						div.row
							div(v-for="chip in 3" :key="chip")
								span.orgcombo-org Joy Division
								span.orgcombo-role Manager
				q-input(outlined dense placeholder="Add member")
					template(v-slot:append)
						q-btn(icon="add" flat dense)
	

q-table.q-ma-sm.main-table(
	:rows="rows2"
	:columns="columns2"
	row-key="id"
	)
	//- template(v-slot:top)
	template(v-slot:header="props")
		q-tr
			q-th icon
			q-th(v-for="col in props.cols" :key="col.fieldname")
				| {{ col.label }}
				//- | {{ col.fieldname }}
				//- | {{ col.type }}
			//- q-th
			//- 	q-btn(icon="add_circle_outline" dense)
	template(v-slot:body="props")
		q-tr
			q-td
				q-skeleton(type="QAvatar" size="36px")
			
			template(v-for="col in props.cols" :key="col.fieldname")
				//- div {{ props.row[1]?.[col.fieldname] }}
				q-td.table-cell {{ props.row[1]?.[col.fieldname] }}
		q-tr
			q-td(colspan="100%")
				q-input(outlined dense placeholder="Add member")
					template(v-slot:prepend)
						q-btn(icon="checklist" flat dense)
					template(v-slot:append)
						q-btn(icon="add" flat dense)
		q-tr(v-if="true")
			q-td(colspan="100%")
				q-item.bg-amber
					q-item-section
						q-breadcrumbs
							q-breadcrumbs-el(label="Home" icon="home")
							q-breadcrumbs-el(label="Components" icon="widgets")
							q-breadcrumbs-el(label="Breadcrumbs")
				div.row
					div.col
						general-table(
							:columns="resource"
							:rows="Object.entries(props.row[1]?.resource)"
							:options="options"
							:type="`container_resource`"
							@send_server_data="send_server_data($event)"
						)
					resource-container

								

</template>

<script>
import { mapGetters } from 'vuex'
import memberMenu from './member-menu.vue'
import resourceContainer from '../resource/resourceContainer.vue'
import generalTable from './general_table.vue'

export default {
	methods: {
		send_server_data(event) {
			console.log(event)
		}
	},
	components: {
		memberMenu,
		resourceContainer,
		generalTable
	},
	computed: {
		...mapGetters(['selected_workspacedata']),
		rows() {
			return Object.entries(this.selected_workspacedata.entity_group)
		},
		rows2() {
			return Object.entries(this.selected_workspacedata.resource_container)
		}
	},
	data() {
		return {
			columns_second: this.resource_task,
			tab: 'management',
			resource: [
				{fieldname: 'name', label: 'Resource name'},
				{fieldname: 'max', label: 'Max'},
				{fieldname: 'amount', label: 'Amount'},
				{fieldname: 'hardcap', label: 'Hardcap'},
				{fieldname: 'exceed_hardcap_strategies', label: 'Strategies'},
			],
			resource_task: [
				{fieldname: 'resource', label: 'Resource name'},
				{fieldname: 'entity', label: 'Entity'},
				{fieldname: 'amount', label: 'Amount'},
				{fieldname: 'scheduled', label: 'Scheduled Amt'},
				{fieldname: 'hardcap', label: 'Hardcap'},
				{fieldname: 'exceed_hardcap_strategies', label: 'Strategies'},
				{fieldname: 'schedule', label: 'Schedule'},
			],
			columns: [
				{fieldname: 'name', label: 'Entity name'},
				{fieldname: 'relationship', label: 'Relationships'},
				{fieldname: 'task', label: 'Tasks'},
				{fieldname: 'entity', label: 'Members'},
				{fieldname: 'permissions', label: 'Permissions'},
				{fieldname: 'allocation', label: 'Allocations'},
				{fieldname: 'allocation', label: 'Resources'},
				{fieldname: 'request', label: 'Resource Request'} 
			],
			columns2: [
				{fieldname: 'name', label: 'Container name'},
				{fieldname: 'resource', label: 'Resource'},
				{fieldname: 'task', label: 'Task'},
				{fieldname: 'entity', label: 'Members'},
			],
			options: [
				'Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'
			]
		}
	}
}
</script>

<style>
.table-cell {
	cursor: pointer;
	white-space: normal !important;
	text-align:center;
}

.table-row {
	box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
}

.left-view {
	position: relative;
}

.settings {
	position: absolute;
	top: 0;
	right: 0;
	z-index: 1000;
}
</style>