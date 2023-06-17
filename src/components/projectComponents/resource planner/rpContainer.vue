<template lang="pug">
general-table(
	:rows="rows"
	:columns="columns"
)
</template>

<script>
import { mapGetters } from 'vuex'
import generalTable from './table.vue'
import { date } from 'quasar'

export default {
	components: {
		generalTable
	},
	computed: {
		...mapGetters(['selected_workspacedata']),
		columns() {
			let x = [
				{name: 'member', label: 'Member'},
				{name: 'actions', label: 'Actions'},
				{name: 'allocated', label: 'Allocated', field:'mon'},
				{name: 'scheduled', label: 'Scheduled',field:'scheduled'},
				{name: 'actual', label: 'Actual',field:'actual'}
				]
			let y = Date.now()
			for(let i=0; i<7; i++) {
				let z = date.addToDate(Date.now(), { days: i })
				let month = date.formatDate(z, 'MM')
				let day = date.formatDate(z, 'D')
				let week_day = date.formatDate(z, 'dd')
				console.log(z, month, day)
				x.push({
					month: month,
					day: day,
					label: `${week_day} ${day} `,
					style: `width: 40px`
				})	
			}
			return x
		},
		rows() {
			let x = [{
				member: '61355552389a7e7a1d45dec7'
			}]
			return x
		}
	}
}
</script>

<style>

</style>