<template lang="pug">
//- q-btn(@click="isvisible_filter=true") FILTER
//- div {{ selected_workspacedata.field }}
q-scroll-area(style="height:100vh").q-pa-md
	main-table(
		v-if="true"
		v-for="board in Object.entries(selected_workspacedata.board)" :key="board[0]"
		:board_id="board[0]"
		:workspace_id="this.userstate.selected_workspace"
		:board="board[1]"
	@update_cell="update_cell($event)"
	@create_task="create_task($event)"
	@create_field="create_field($event)"
	)

	//- settings(
	//- 	v-if="false"
	//- 	:field="computed_field"
	//- )
	//- q-btn(
	//- 	icon="settings"
	//- 	@click="isvisible_automation=true"
	//- 	)
	q-dialog(v-model="isvisible_automation")
		automation-settings

	//- kanban(
	//- 	v-if="true"
	//- 	:tasks="kanban_tasks"
	//- 	:field="computed_field"
	//- )

q-dialog(v-model="isvisible_filter")
	automation-container(
		:field="Object.keys(computed_field)"
	)


</template>

<script>
import { mapGetters } from 'vuex'
import mainTable from '../taskComponents/main table/maintable.vue'
import kanban from '../taskComponents/kanban/kanban'
import settings from '../taskComponents/fieldsettings/fieldsettings.vue'
import automationSettings from '../taskComponents/fieldsettings/automationsettings.vue'
import automationContainer from '../automation/automationContainer.vue'


export default {
	components: {
		mainTable,
		settings,
		kanban,
		automationSettings,
		automationContainer
	},
	data() {
		return {
			isvisible_filter: false,
			isvisible_automation: false
		}
	},
	computed: {
		...mapGetters(['selected_workspacedata', 'userstate', 'array_fields']),
		kanban_tasks() {
			return Object.values(this.selected_workspacedata.board).reduce((prev,cur)=> {
				Object.entries(cur.task).forEach(ele => prev[ele[0]] = ele[1])
				return prev
			},{})
		}
	},
	methods: {
		create_task({board_id}) {
			let new_task = Object.entries(this.selected_workspacedata.field).reduce(
				(prev, cur) => {prev[cur[0]] = cur[1]?.default; return prev}, {}
				)
			let id = Math.floor(Math.random() * 60)
			this.$store.commit('mutate_set', {
				string: `workspacedata.${this.userstate.selected_workspace}.board.${board_id}.task.${id}`,
				value: new_task
			})
		},
		update_cell({task_id, selected_field, input, board_id, operation='set', type}) {
			
			
			// console.log(task_id, selected_field, input, board_id, operation, type)
			// var data = (type != null) ? {[type]: {[selected_field]: input}}: {[selected_field]: input}
			// var old = this.selected_workspacedata.board[board_id].task[task_id][selected_field]
			// var data_old = (type != null) ? {[type]: {[selected_field]: old}}: {[selected_field]: old}
			// this.$api({
			// 	method: 'patch',
			// 	url: `/workspace/${this.userstate.selected_workspace}/board/${board_id}/task/${task_id}`,
			// 	data: {
			// 		task: data,
			// 		task_old: data_old
			// 	},
			// 	headers : {
			// 	'Content-Type': 'application/json',
			// 	Authorization: `Bearer ${this.$store.state.auth}`
			// 	}
			// 	}).then((response)=>{
			// 		console.log(response);
			// 	}).catch((error) => {
			// 		null
			// 	})
			// console.log({
			// 		task: data,
			// 		task_old: data_old
			// 	})
			
			this.$store.commit('mutate_task', {
					workspace_id: this.userstate.selected_workspace,
					board_id: board_id,
					task_id: task_id,
					attr: selected_field,
					operation: operation,
					value: input,
					type: type
				})
			if(type=='date') {
				input = new Date(input)
			}
			else if(type=='daterange') {
				input = {
					start: new Date(input.from),
					end: new Date(input.to)
				}
			}
			
		}
	}	
}
</script>

<style>

</style>