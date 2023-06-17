<template lang="pug">
q-dialog(v-model="isvisible_todomodal")
	q-card
		q-card-section
			q-input(label="title" outlined)
		q-card-section
			q-input(label="description" outlined)
		q-card-section
			q-select(
				filled
        v-model="involved"
        use-input
        input-debounce="0"
        label="Simple filter"
        :options="options"
        @filter="filterFn"
        style="width: 250px"
				use-chips
			)
		q-card-section
			q-input(readonly v-model="days" outlined)
				q-menu(v-model="isvisible_date")
					q-date(v-model="days" multiple)
		q-card-actions
			q-btn(unelevated) Save
			q-btn(unelevated) Cancel
	

</template>

<script>
import { mapFields } from 'vuex-map-fields';
import { ref } from 'vue';

export default {
	props: ['serverdata'],
	mounted() {
		this.options = this.member_names
	},
	methods: {
		filterFn (val, update, abort) {
			if (val === '') {
				update(() => {
					this.options = this.member_names
					console.log(this.options)
				})
				return
			}
			update(() => {
				const needle = val.toLowerCase()
				this.options = this.member_names.filter(v => v.label.toLowerCase().indexOf(needle) > -1)
				console.log(this.member_names.filter(v => v.label.toLowerCase().indexOf(needle) > -1))
				console.log(this.options)
			})
      }
		},
	computed: {
		...mapFields(['isvisible_todomodal']),
		member_names() {
			console.log(this.serverdata.members)
			return Object.entries(this.serverdata.members).map(
				ele => { return {
					label: ele[1].nick,
					value: ele[0]
    		}
			})
		},
	},
	data() {
		return {
			options: null,
			involved: null,
			isvisible_date: false,
			days: ['2021/02/01'],
		}
	}
}
</script>

<style>

</style>
