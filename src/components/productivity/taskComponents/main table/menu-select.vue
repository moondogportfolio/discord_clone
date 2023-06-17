<template lang="pug">
q-card
	q-card-section
		q-select(
			filled
			v-model="modelMultiple"
			
			:options="select_options"
			dense
			outlined
			use-input
			label="Add resource to container"
			input-debounce="0"
			@filter="filterFn"
			)
			template(v-slot:no-option)
				q-item
					q-item-section.text-grey No results
			template(v-slot:after)
				q-btn(
					round
					dense
					flat
					icon="add"
					@click="emit_event"
					)
</template>

<script>
export default {
	created() {
		this.select_options = this.options
	},
	methods: {
		filterFn (val, update) {
				if (val === '') {
					update(() => {
						this.select_options = this.options

						// here you have access to "ref" which
						// is the Vue reference of the QSelect
					})
					return
				}

				update(() => {
					const needle = val.toLowerCase()
					this.select_options = this.options.filter(v => v.toLowerCase().indexOf(needle) > -1)
				})
			},
		emit_event() {
			this.$emit('emit_value', this.modelMultiple
			)
		},
	},
	emits: ['emit_value'],
	props: ['options', 'type'],
	data() {
		return {
			modelMultiple: null,
			select_options: null
		}
	}

}
</script>

<style>

</style>