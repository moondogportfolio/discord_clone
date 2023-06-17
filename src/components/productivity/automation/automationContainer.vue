<template lang="pug">
q-card.text-h5.q-ma-sm.q-pa-lg
	div {{ logic_object }}
	q-card-section
		div triggers:
		div.row.q-ml-md(
			v-for="(condition, index) in logic_object.triggers"
			:key="index"
			)
			span.automation-placeholder(v-if="!condition?.label") trigger
				q-menu
					q-item(clickable @click="add_trigger(index, 'val_update')") Field value update
					q-item(clickable) Date arrives
					q-item(clickable) Task created
					q-item(clickable) Task deleted
					q-item(clickable) Task moved
			template(v-else)
				div.automation-placeholder {{ condition?.label }} 
				div in 
				div.automation-placeholder scope
					q-menu
						q-item(clickable) Board
						q-item(clickable) Task
						q-item(clickable) Group
			
			//- template(v-if="index%2==0 && index!=triggers_length-1")
			//-   div {{ index==0? 'if': 'else-if' }}
			//-   logic.q-ml-md(
			//-     :condition="condition"
			//-     :depth="`triggers[${index}]`"
			//-   )
		div.q-ml-md(style="opacity: 0.2") Add new
			q-menu
				q-item(clickable @click="add_trigger(triggers_length, 'val_update')") Field value update
				q-item(clickable) Date arrives
				q-item(clickable) Task created
				q-item(clickable) Task deleted
				q-item(clickable) Task moved
		div conditions:
		div.q-ml-md(v-for="(condition, index) in logic_object.conditions" :key="index")
			template(v-if="index%2==0 && index!=conditions_length-1")
				div {{ index==0? 'if': 'else-if' }}
				logic.q-ml-md(
					:condition="condition"
					:depth="`conditions[${index}]`"
				)
		div effect
</template>

<script>
import jsonLogic from 'json-logic-js'
import logic from './logic.vue'

export default {
	components: { 
		logic,
	},
	methods: {
		add_trigger(index, trigger) {
			console.log(index, trigger)
			this.$store.commit('mutate_set', {
				string: `logic.triggers[${index}]`,
				value: this.translation[trigger]

			})
		}
	},
	data() {
		return {
			isvisible_object: true,
			translation: {
				val_update: {
					label: `Δvalue`,
					trigger: 'val_update',
					scope: {
						board: null,
						group: null,
						task: null
					}
				}
			},
			object_option: ['Task', 'Field']
		}
	},
	computed: {
		conditions_length() {
			return this.logic_object.conditions.length
		},
		triggers_length() {
			return this.logic_object.triggers.length
		},
		logic_object() {
			return this.$store.state.logic
		},
	}

}
</script>

<style>
.sentence-filler {
	color: lightgrey;
}

.automation-placeholder {
	/* min-width: 100px; */
	width: fit-content;
	border-bottom: 2px solid black;
	color: lightblue;
	cursor: pointer;
	margin: 0 5px;
}

.automation-variable {
	border-bottom: 2px solid black;
	color: lightblue;
}

.sentence {
	display: flex;
	flex-wrap: wrap;
	gap: 5px;
}
</style>