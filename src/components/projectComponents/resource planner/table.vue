<template lang="pug">


q-card-section.row.resource-container
	div(style="width: 350px").row
		div.col-grow
		div.resource-item-left alloc
		div.resource-item-left sched
		div.resource-item-left actual
	div.resource-item-right(v-for="item in 14" :key="item") {{ item }}
q-card-section
	q-virtual-scroll(:items="rows" separator)
		template(v-slot="{ item, index }")
			div.row
				q-expansion-item(
					icon="perm_identity"
					:key="index"
					:label="item.member"
					style="width: 350px"
					@after-show="isexpanded_member[item.member] = true"
					@before-hide="isexpanded_member[item.member] = false"
					)
					div.row.resource-task-container(v-for="subitem in 16" :key="subitem")
						div.col-grow {{ subitem }}
						div.resource-item-left 15
						div.resource-item-left 120
						div.resource-item-left 150
						q-menu(context-menu)
							menu-resource

				div.col(v-if="isexpanded_member[item.member]" )
					div(style="height:48px;")
					div.resource-schedule-container(v-for="subitem in 16" :key="subitem")
						div.calendar-cell
					//- template(v-if="")


		

</template>

<script>
import { date } from 'quasar';
import menuResource from './menu-resource.vue'
import { mapGetters } from 'vuex'

const maxSize = 10
const heavyList = []
import { debounce } from 'quasar'

for (let i = 0; i < maxSize; i++) {
heavyList.push({
	label: 'Option ' + (i + 1)
})
}


export default {
	props: ["rows", "columns"],
	setup() {
		return {
			heavyList
		}
	},
	components: {
		menuResource
	},
	computed: {
		...mapGetters(['selected_workspacedata'])
	},
	data() {
		return {
			damn: 'DAMN',
			isexpanded_member: {}
		}
	},
	methods: {
		getHourDiff(start, end) {
			console.log(start, end);
			let parsed_start = date.extractDate(start, 'HH:mm')
			let parsed_end = date.extractDate(end, 'HH:mm')
			return date.getDateDiff(parsed_end, parsed_start, 'hours')
		}
	},
	created() {
		
			this.rows.forEach(ele=>{
				console.log(ele)
				this.isexpanded_member[ele.member]=false
			})
			console.log(this.isexpanded_member['61355552389a7e7a1d45dec7'])
			this.date = date
		},
}
</script>

<style scoped>

.resource-container {
	min-width: 960px;
}

.resource-schedule-line {
	position: relative;
}

.calendar-cell {
	background: bisque;
	height: 24px;
	width: 400px;
	left: 40px;
	position: absolute;
	cursor: pointer;
}

.resource-task-container {
	position: relative;
	height: 40px;
	cursor: pointer;
}

.resource-schedule-container {
	position: relative;
	height: 40px;
}

.resource-item-left {
	width: 50px;
}

.resource-item-right {
	width: 40px;
	text-align: right;
}

.resource-top {
	display: grid;
	grid-template-columns: 100px repeat(4, 1fr) repeat(14, 36px)
}

.wrapper {
	background: beige;
}

.task-cell {
	background: blanchedalmond;	
}

.table-cell {
	white-space: normal;
	text-align:center
}

.delivered {
	border-left: 5px solid black;
}

.round-border-4 {
	border-radius: 0 0 0 10px;
}

.round-border-3 {
	border-radius: 0 0 10px 0;
}

.round-border-2 {
	border-radius: 0 10px 0 0;
}

.round-border-1 {
	border-radius: 10px 0 0 10;
}
</style>