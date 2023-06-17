<template lang="pug">
//- //- div {{ input_val }}
//- div ROWS {{ board.task }}
//- div COLS {{ columns }}
//- div FIELDS {{ field }}
//- div filtered {{ filtered_rows }}
//- div {{ task_id }} {{ selected_field }}
//- div board {{ board }}
//- div {{ status_groups }}

q-btn(@click="iscollapsed_table=!iscollapsed_table")
q-table.q-ma-sm.main-table(
	:rows="rows"
	:columns="columns"
	row-key="id"
	:hide-pagination="!iscollapsed_table"
	)
	template(v-slot:top)
		menu-board-container(
			:board_id="board_id"
			@add_task_dialog="isvisible_addtask=true"
			)
	template(v-slot:header="props")
		template(v-if="iscollapsed_table")
			q-tr
				q-th.boss-header
					
				q-th(v-for="col in props.cols" :key="col.fieldname")
					| {{ col.label }}
					q-menu
						menu-table-header.table-menu
					//- | {{ col.fieldname }}
					//- | {{ col.type }}
				q-th
					q-btn(icon="add_circle_outline" dense)
	template(v-slot:body="props")
		template(v-if="iscollapsed_table")
			//- q-tr
			//- 	q-td( colspan="100%")
			q-tr
				q-td.id-cell
					div.row.full-height(style="align-items: center")
						div.col-shrink.task-selector
							div
								div
						div.col {{ props.row.id }}
						q-menu.table-context-menu.table-menu(
							context-menu
							@before-show="hide_menu"
							)
							menu-cell-task(
								@view_task_details="show_menu_task(props.row)"
							)
				template(v-for="col in props.cols" :key="col.fieldname")
				
					q-td.table-cell(
						style="white-space: normal; text-align:center"
						@click="set_current_cell(props.row.id, col.fieldname)"
						)
						data-displayer(
							:row="props.row"
							:col="col"
							:date="date"
							)
						//- template(v-if="col.type=='checkbox'")
						//- 	div ✅: {{ checkbox_props(props.row?.[col.fieldname], true) }}
						//- 	div ❌: {{ checkbox_props(props.row?.[col.fieldname], false) }}
						//- 	div {{ props.row?.[col.fieldname] }}
						//- 	//- q-checkbox(v-model="checkbox_temp[col.fieldname]")
						//- template(v-else-if="props.row?.[col.fieldname]!=null")
						//- 	template(v-if="col.fieldname=='group'")
						//- 		q-chip(v-for="group in props.row?.[col.fieldname]" :key="group") {{ group }}
						//- 	template(v-else-if="col.type=='daterange' && props.row?.[col.fieldname]!= null")
						//- 		div.text-white.q-pa-xs(:style="schedule_bar(props.row?.[col.fieldname])")
						//- 			| {{ date.formatDate(props.row?.[col.fieldname].from, 'MMM D -') }}
						//- 			| {{ date.formatDate(props.row?.[col.fieldname].to, 'MMM D') }}
						//- 	div(v-else-if="col.type=='date'") 
						//- 		|	{{ date.formatDate(props.row?.[col.fieldname], 'MMM D') }}
						//- 	div(v-else)
						//- 		|	{{ props.row?.[col.fieldname] }}
						//- 	//- | {{ props.cols[index].type }}
						//- div.text-grey(v-else) ∅
						q-menu.table-context-menu.table-menu(
							context-menu
							@before-show="hide_menu"
							)
							main-table-menu(
								@view_task_details="show_menu_task(props.row)"
							)
								
						q-menu(
							v-if="isclone(props.row.id, col.fieldname)"
							anchor="bottom middle"
							self="top middle"
							@before-show="hide_context_menu"
							)
							menu-color(
								v-if="col.type=='color'"
								:value="props.row?.[col.fieldname]"
								@update_cell="emit_update($event)"
								)

							menu-category(
								v-else-if="col.fieldname=='tag'"
								)
							menu-group(
								v-else-if="col.fieldname=='group'"
								:board_id="board_id"
								:workspace_id="workspace_id"
								:task_id="props.row.id"
								)
							menu-checkbox(
								v-else-if="col.type=='checkbox'"
								:value="props.row?.[col.fieldname] || {}"
								@add_value_subvalue="emit_update($event, col.type, 'merge')"
							)
							menu-slider(
								v-else-if="['progress', 'granularity'].includes(col.type)"
								:value="props.row?.[col.fieldname]"
								@update_cell="emit_update($event)"
								:type="col.type"
							)
							menu-input(
								v-else-if="['number','text'].includes(col.type)"
								:value="props.row?.[col.fieldname]"
								:type="col.type"
								@update_cell="emit_update($event, col.type)"
								)
							menu-status(
								v-else-if="col.fieldname=='status'"
								:options="field[col.fieldname].options"
								@update_cell="emit_update($event)"
								)
							menu-date(
								v-else-if="['daterange','date'].includes(col.type)"
								:value="props.row?.[col.fieldname]"
								:now="date.formatDate( Date.now(), 'YYYY/MM/DD')"
								@update_cell="emit_update($event, col.type)"
								:type="col.type"
							)
							//- q-card-section.row(v-else)
							//- 	q-input.col(v-model="input_val" outlined)
							//- 	q-btn.col-shrink.q-ml-sm(@click="emit('update_cell', input_val)") OK
						
				q-td
	template(v-slot:bottom-row="props" v-if="iscollapsed_table")
		q-tr
			q-td AGGREGATES
			template(v-for="(col, index) in props.cols" :key="col.fieldname")
				q-td.table-bottom-cell 
					span(v-if="col.type == 'number'") {{ rows.reduce((prev, cur) => prev+= cur[col.fieldname], 0) }}
						.text-caption SUM
					div.status-grid(v-else-if="col.fieldname == 'status'" :style="status_groups_size")
						span.col(
							v-for="group in Object.entries(status_groups)"
							:key="group[0]"
							:style="`background: ${field.status.options.find(ele=>ele.name==group[0])?.color || 'gray' }; height:32px`"
							)

					span(v-else-if="col.field == 'date-start'") {{ date.formatDate(date.getMinDate(...rows.reduce((prev, cur) => prev.concat([cur['date-start']]) , [])), 'YYYY/MM/DD') }}
					span(v-else-if="col.field == 'date-end'") {{ date.formatDate(date.getMaxDate(...rows.reduce((prev, cur) => prev.concat([cur['date-end']]) , [])), 'YYYY/MM/DD') }}
			q-td
		q-tr
			q-td( colspan="100%")
				q-input(outlined dense placeholder="Add task")
					template(v-slot:append)
						q-btn(icon="add" dense)




menu-task.q-ma-sm(
	style="position:absolute; right:0; top:0;"
	v-if="isvisible_menutask"
	:row="menu_task"
	:columns="columns"
	:date="date"
	)
	
q-dialog(v-model="isvisible_addtask" separate-close-popup)
	q-card
		q-card-section
			q-input(placeholder="Task name" outlined v-model="add_task_input")
			//- q-input(v-for="")
		q-card-actions
			q-btn(@click="create_task_local") Add task


</template>

<script>
import { date, uid } from 'quasar'
import mainTableMenu from './maintable menu.vue'
import menuStatus from './menu-option.vue'
import menuStatusFieldEdit from './menu-status-field-edit.vue'
import menuCategory from './menu-tag.vue'
import menuGroup from './menu-group.vue'
import menuColor from './menu-color.vue'
import menuDate from './menu-daterange.vue'
import menuInput from './menu-input.vue'
import menuFormula from './menu-formula.vue'
import menuTask from './menu-task.vue'
import menuSlider from './menu-slider.vue'
import menuBoardContainer from './menu-board-container.vue'
import menuTableHeader from './menu-table-header.vue'
import menuCheckbox from './menu-checkbox.vue'
import dataDisplayer from './composition/data_displayer.vue'
import jsonLogic from 'json-logic-js'
import menuCellTask from './menu-cell-task.vue'


import create_task from './composition/create_task.js'
import { mapGetters } from 'vuex'


export default {
	setup() {
		return {
			create_task
		}
	},
	props: ['board_id', 'board', 'workspace_id'],
	emits: ['create_field', 'update_cell', 'create_task'],
	components: {
		menuCellTask,
		dataDisplayer,
		mainTableMenu,
		menuStatus,
		menuTask,
		menuStatusFieldEdit,
		menuCategory,
		menuGroup,
		menuInput,
		menuColor,
		menuDate,
		menuFormula,
		menuSlider,
		menuTableHeader,
		menuCheckbox,
		menuBoardContainer
	},
	created() {
			this.date = date
		},
	computed: {
		...mapGetters(['user_id', 'userstate']),
		field() {
			let x = {}
			Object.entries(this.board.field).forEach(ele => {
				if(ele[0]=='checkbox') {
					ele[1].forEach(inner_ele=> this.checkbox_temp[inner_ele.fieldname] = false)
				}
				if(['number', 'text','color', 'date', 'daterange', 'resource', 'involved', 'checkbox'].includes(ele[0])) {
					ele[1].forEach(inner_ele=> x[inner_ele.fieldname] = inner_ele)
				}
				else {
					x[ele[0]] = ele[1]
				}
			})
			return x
		},
		status_groups_size() {
			return `grid-template-columns: ${Object.entries(this.status_groups).map(ele => ele[1].length).join('fr ').concat('fr')}`
		},
		status_groups() {
			return _.groupBy(this.board.task, 'status')
		},
		columns() {
			// return Object.values(this.field).filter(ele=>[
			// 	'status', 'involved', 'date', 'daterange',
			// 	'budget'
			// 	].includes(ele.fieldname))
			return Object.values(this.field)
		},
		rows() {
			// return Object.entries(this.board.task).forEach(ele => {
			// 	ele[1].id = ele[0];
			// 	return ele[1]
			// 	}
			// 	)
			let x = {}
			Object.entries(this.board.task).forEach(task => {
				x[task[0]] = {}
				x[task[0]].id = task[0]
				Object.entries(task[1]).forEach(field => {
					if(['number', 'text','color', 'resource', 'involved', 'checkbox'].includes(field[0])) {
						Object.entries(field[1]).forEach(subfield=> {
							x[task[0]][subfield[0]] = subfield[1];
						})
					}
					else if(field[0]=='date') {
						Object.entries(field[1]).forEach(subfield=> {
							console.log(subfield)
							subfield[1] = new Date(subfield[1])
							subfield[1] = subfield[1].toLocaleString()
							console.log(subfield[1])
							x[task[0]][subfield[0]] = subfield[1];
						})
						console.log(field[0])
					}
					else if(field[0]=='daterange') {
						Object.entries(field[1]).forEach(subfield=> {
							x[task[0]][subfield[0]] = subfield[1].start ?
								{from: subfield[1].start , to:subfield[1].end} :
								subfield[1]
						})
					}
					else if(['status', 'completion_dependency', 'group', 'granularity', 'progress'].includes(field[0])){
						x[task[0]][field[0]] = field[1];
					}
				})
			})
			return Object.values(x)
				
		},
		filtered_rows() {
			let rules = this.$store.state.logic.conditions
			return this.rows.filter(ele => {
				console.log(jsonLogic.apply(rules, {task: ele}))
				return jsonLogic.apply(rules, {task: ele})[0]
			})
		}
	},
	methods: {
		isclone(id, field) {
			console.log()
			return this.board.task[id].meta?.outgoing_ref?.[field] == null
		},
		show_menu_task(row) {
			this.isvisible_menutask=!this.isvisible_menutask
			this.menu_task = row
		},
		checkbox_props(item, bool) {
			if(item==null) return 0
			return Object.entries(item).filter(ele=>ele[1] == bool).length
		},
		create_task_local() {
			// this.create_task(
			// 	this.add_task_input,
			// 	this.$api,
			// 	this.$store.state.auth,
			// 	this.board_id,
			// 	this.workspace_id,
			// )
			this.$store.commit('mutate_set', {
          string: `workspacedata.${this.userstate.selected_workspace}.board.${this.board_id}.task.tentative-${uid()}`,
          value: {
						type: 1,
						board: this.board_id,
						meta: {
							creator:this.user_id
						}
					}
        })
		},
		schedule_bar(date) {
			let from_diff =  this.date.getDateDiff(date.from, Date.now(), 'days')
			let to_diff =  this.date.getDateDiff(date.to, Date.now(), 'days')
			if(from_diff < 0 && to_diff < 0) return `background: black;`
			else if(from_diff > 0 && to_diff > 0) return `background: blue;`
			else {
				let first_stop = `${Math.trunc((-from_diff/(-from_diff+to_diff))*100)}%`
				return `background: linear-gradient(to right, rgb(102, 204, 255) ${first_stop}, rgb(28, 31, 59) ${first_stop});`
			}
		},
		hide_context_menu() {
			document.querySelector('.table-context-menu')?.parentElement.remove()
		},
		hide_menu() {
			return
			document.querySelector('.table-menu')?.parentElement.remove()
		},
		emit_update(option, type=null, operation='set') {
			this.$emit('update_cell', {
				task_id: this.task_id,
				selected_field: this.selected_field,
				operation: operation,
				input: option,
				board_id:this.board_id,
				type: type
				})
		},
		set_current_cell(task, selected_field) {
			this.task_id = task;
			this.selected_field = selected_field;
		}
	},
	data() {
		return {
			menu_task: null,
			checkbox_temp: {},
			add_task_input: null,
			isvisible_addtask: false,
			isvisible_menutask: false,
			getMinDate: null,
			input_val:null,
			task_id: null,
			selected_field: null,
			edit_status_labels: true,
			iscollapsed_table: true
		}
	}

}
</script>

<style>

.table-header {
	text-align: center;
}

.table-bottom-cell {
	text-align: center;
}

.table-cell:hover {
	background: cornsilk;
}

.status-grid {
	display: grid;
}

.id-cell {
	padding-left: 0 !important;
}

.task-selector {
	display: contents;
}

.task-selector div {
	width: 8px;
	height: 100%;
	background: rgb(184, 228, 255);
	margin-right: 5px;
	transition: width .07s cubic-bezier(0, 0, 0.35, 1);
	position:relative;
	will-change: width;
	overflow: hidden;
	
	border-radius: 0 3px 3px 0;
}

.task-selector > div:hover {
	width: 35px;
}

.task-selector div div {
	position: absolute;
	top: 50%;
	transform: translateY(-50%);
	left: 9px;
	height: 14px;
	width: 14px;
	background-color: rgba(0,0,0,.2);
	outline: 1px rgba(255,255,255,.2) solid;
	display: flex;
	justify-content: center;
	align-items: center;
}

.boss-header {
	padding: 0px !important;
}


.table-menu {
	width: 300px;
}

</style>