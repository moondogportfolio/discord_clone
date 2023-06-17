<template lang="pug">
q-card.q-ma-sm.shadow-1
	q-card-section(v-if="false")
		q-table(:columns="res_columns" :rows="resources" style="width:700px")
			template(v-slot:header="props")
				q-tr
					q-th(v-for="col in props.cols" :key="col.fieldname")
						| {{ col.label }}
			template(v-slot:body="props")
				q-tr
					template(v-for="col in props.cols" :key="col.fieldname")
						q-td.table-cell {{ props.row?.[col.fieldname] || '∅' }}
			template(v-slot:bottom-row="props")
				q-tr
					q-td( colspan="100%")
						q-input(
							outlined
							dense
							placeholder="Add resource"
							v-model="input_new_resource_name"
							)
							template(v-slot:append)
								q-btn(icon="add" dense flat @click="server_create_resource")



	q-card-section
		q-table.main-table(:rows="rows" :columns="columns" row-key="id")
			template(v-slot:header="props")
				q-tr
					q-th(v-for="col in props.cols" :key="col.fieldname")
						| {{ col.label }}
			template(v-slot:body="props")
				q-tr
					q-td.text-grey(colspan="3") Event name, Service for Mr. Grey
					q-td.text-grey.text-right(colspan="3") Transaction ID 098901283-CD
				q-tr
					template(v-for="col in props.cols" :key="col.fieldname")
						q-td.text-grey.table-cell {{ props.row?.[col.fieldname] }}
			template(v-slot:bottom-row="props")
				q-tr
					q-td( colspan="100%")
						q-input(outlined dense placeholder="New TX: Set description")
							template(v-slot:append)
								q-btn(icon="add" dense flat @click="add_tx")
							
q-dialog(v-model="isvisible_addtx")
	menu-add-resource(
		:resources="resources"
	)

</template>

<script>
import { mapGetters } from 'vuex'
import menuAddResource from './menu-add-resource.vue'

export default {
	created() {
		console.log(this.$store.state)
	},
	components: {
		menuAddResource
	},
	computed: {
		...mapGetters(['selected_workspacedata', 'userstate']),
		resources() {
			return this.selected_workspacedata.resource
		}
	},
	methods: {
		add_tx() {
			this.isvisible_addtx = true;
		},
		async server_create_resource() {
			await this.$api({
        method: 'post',
        url: `/workspace/${this.userstate.selected_workspace}/resource`,
        data: {
					name: this.input_new_resource_name
        },
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
        }
      }).then((response)=>{
				this.$store.commit('mutate_set', {
					string: `workspacedata.${this.userstate.selected_workspace}.resource.${response.data}`,
					value: {
						name: this.input_new_resource_name,
						budget: 0
					}
				})
				console.log(response);
      }).catch((error) => {
          null
      })
			this.input_new_resource_name = null;
		}
	},
	data() {
		return {
			isvisible_addtx: false,
			input_new_resource_name: null,
			tab: 'resource_in',
			res_columns: [
				{label: 'Name', fieldname: 'name'},
				{label: 'Budget', fieldname: 'budget'},
				{label: 'Hardcap', fieldname: 'hardcap'},
				],
			columns: [
				{label: 'Status', fieldname: 'b'},
				{label: 'Resource Out', fieldname: 'a'},
				{label: 'Resource In', fieldname: 'b'},
				{label: 'Date', fieldname: 'b'},
				{label: 'Entity Out', fieldname: 'b'},
				{label: 'Entity In', fieldname: 'c'},
				],
			rows: [
				{a: 1, b: 2}, {a: 3, b: 4}
			]
		}
	}
}
</script>

<style>
.table-cell {
	text-align: center;
}

</style>