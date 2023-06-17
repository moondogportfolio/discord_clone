<template lang="pug">
q-card(style="width:800px;")
	q-card-section.column.fit.q-pa-none
		q-tabs.col-shrink(
				dense
				v-model="tab"
				class="text-grey"
				active-color="primary"
				inline-label
				indicator-color="primary"
				align="justify"
				narrow-indicator
		)
				q-tab(name="tx_details" label="TX Details")
				q-tab(name="resource_in" label="Resource In")
				q-tab(name="resource_out" label="Resource Out")
		q-separator
		q-tab-panels.col(v-model="tab" keep-alive)
				q-tab-panel.q-pa-none(name="tx_details")
					menu-tx-details(
						:details="details"
					)
				q-tab-panel.q-pa-none(name="resource_in")
					menu-resource-in(
						:resources="resources"
						:rows="resources_input.resource_in"
						@add_transaction_item="add_transaction_item($event, 'resource_in')"
						@update_cell="update_cell($event, 'resource_in')"
					)
				q-tab-panel.q-pa-none(name="resource_out")
					menu-resource-in(
						:resources="resources"
						:rows="resources_input.resource_out"
						@add_transaction_item="add_transaction_item($event, 'resource_out')"
						@update_cell="update_cell($event, 'resource_out')"
					)
				
		q-card-section
				q-btn(@click="server_create_tx") Save TX
</template>

<script>
import menuResourceIn from './menu-resource-in.vue';
import menuTxDetails from './menu-tx-details.vue';
import {date} from 'quasar';
import { mapGetters } from 'vuex';
const {formatDate} = date;

export default {
	components: {
		menuTxDetails,
		menuResourceIn,
	},
	computed: {
		...mapGetters(['userstate']),
	},
	methods: {
		async server_create_tx() {
			let data = Object.assign({}, this.details, this.resources_input);
			console.log(JSON.stringify(data))
			await this.$api({
        method: 'post',
        url: `/workspace/${this.userstate.selected_workspace}/transaction`,
        data: data,
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
        }
      }).then((response)=>{
				this.$store.commit('mutate_set', {
					string: `workspacedata.${this.userstate.selected_workspace}.transaction.${response.data}`,
					value: data
				})
				console.log(response);
      }).catch((error) => {
          null
      })
			this.input_new_resource_name = null;
		},
    add_transaction_item(input_amount, res_input) {
			let resource = this.resources_input[res_input]
			let len = this.resources_input[res_input].length
      resource.push({
        amount: Number(input_amount) || 0,
        resource: resource?.[len-1]?.resource,
        transfer_date: formatDate( Date.now(), 'YYYY-MM-DD HH:mm'),
        entity: resource?.[len-1]?.entity,
        index: len
      })
    },
		update_cell_details({field, value}) {
			this.details[field] = value
		},
		update_cell({value, row, field}, res_input) {
			this.resources_input[res_input][row][field] = value
		}
	},
	props: ['resources'],
	data() {
		return {
			tab: 'resource_in',
			resources_input: {
				resource_out: [],
				resource_in: []
			},
			details: {
				status: null,
				details: null,
				settlement_date: null,
				initiator: null,
				approval: null
			}
		}
	}

}
</script>

<style>

</style>