<template lang="pug">
div {{ sum }}
q-card.q-ma-sm(style="width:400px;")
	q-card-section.distributor-container
			template(v-for="task in tasks" :key="task")
				div {{ task }}
				q-knob(
					v-model="task_model[task].value"
					size="36px"
					color="purple"
					track-color="purple-1"
					@change="update_max($event, task_model[task])"
					)
				div {{ Math.trunc(budget*(task_model[task].value/100)) }} {{ task_model[task].value }}
			template(
				v-for="group in Object.entries(groups)"
				:key="group[0]"
				) 
				div {{ group[0]  }}
				q-knob(
					show-value
					v-model="group_model[group[0]].value"
					size="36px"
					color="green"
					track-color="purple-1"
					@change="update_max($event, group_model[group[0]])"
					)
				div {{ Math.trunc(budget*(group_model[group[0]].value/100))  }} 
				template(v-for="member in group[1]" :key="member")
					div {{ member }}
					q-knob(
						show-value
						v-model="member_model[member].value"
						size="36px"
						color="orange"
						track-color="purple-1"
						@change="update_sub($event, member_model[member], group_model[group[0]])"
						)
					div {{ Math.trunc(budget*(member_model[member].value/100)) }}

		
</template>

<script>
export default {
	methods: {
		update_sub(new_val, obj, parent_obj) {
			parent_obj.sum += new_val - obj.old
			var max = parent_obj.value
			if(parent_obj.sum > max) {
				new_val -= parent_obj.sum - max
				parent_obj.sum = max
				obj.value = new_val
			}
			obj.old = new_val
		},
		update() {
			console.log('UPDATE')
		},
		update_max(new_val, obj) {
			this.sum += new_val - obj.old
			if(this.sum >100) {
				new_val -= this.sum - 100
				this.sum = 100
				obj.value = new_val
			}
			obj.old = new_val
		}
	},
	created() {
		this.tasks.forEach(ele=>this.task_model[ele] = {value: 0, old: 0})
		Object.entries(this.groups).forEach(ele=>{
			this.group_model[ele[0]] = {value: 0, old: 0, sum: 0};
			ele[1].forEach(member=>this.member_model[member] = {value: 0, old: 0})
		})
	},
	data() {
		return {
			sum: 0,
			budget: 10000,
			task_model: {},
			group_model: {},
			member_model: {},
			slider: 0,
			tasks: ['a','b','c'],
			groups: {
				'xasdasdasdasdasd': ['q','w'],
				'y': ['qw','we']
			}
		}
	}
}
</script>

<style>
.distributor-container {
	display: grid;
	grid-template-rows: auto();
	grid-template-columns: 1fr 50px 100px;
	row-gap: 10px;
}




</style>