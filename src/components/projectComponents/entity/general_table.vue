<template lang="pug">
q-table.q-ma-sm.main-table(
		:rows="rows"
		:columns="columns"
		row-key="id"
		hide-pagination
		)
		template(v-slot:top)
		
				q-btn.settings(icon="settings" size="12px" unelevated dense )
		template(v-slot:header="props")
				q-tr
						q-th(v-for="col in props.cols" :key="col.fieldname")
								| {{ col.label }}
								//- | {{ col.fieldname }}
								//- | {{ col.type }}
		//- 		q-th
		//- 			q-btn(icon="add_circle_outline" dense)
		template(v-slot:body="props")
				q-tr
						template(v-for="col in props.cols" :key="col.fieldname")
								//- div {{ props.row[1]?.[col.fieldname] }}
								q-td.table-cell
										div.row(v-if="col.fieldname=='name'")
												q-skeleton(type="QAvatar" size="36px")
												span {{ props.row[1]?.[col.fieldname] }}
										div(v-else) {{ props.row[1]?.[col.fieldname] }}
				q-tr
					q-td(colspan="100%")
						q-select(
							filled
							v-model="modelMultiple"
							multiple
							:options="select_options"
							use-chips
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
	props: ['rows', 'columns', 'options', 'type'],
	emits: ['send_server_data'],
	created() {
		this.select_options = this.options
	},
	methods: {
		emit_event() {
			this.$emit('send_server_data', {
				data: this.modelMultiple,
				type: this.type
			})
		},
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
			}
	},
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