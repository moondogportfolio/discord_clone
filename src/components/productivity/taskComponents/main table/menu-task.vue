<template lang="pug">
q-card.soft-shadow(style="width: 550px;")
	q-card-section.column.fit.q-pa-none
		q-tabs.col-shrink(
			v-model="tab"
			class="text-grey"
			active-color="primary"
			inline-label
			indicator-color="transparent"
			align="justify"
			dense
		)
			q-tab(name="view" label="Card View")
			q-tab(name="updates" label="Updates")
			q-tab(name="approvals" label="Requests")
			q-tab(name="cycle" label="Cycle")
		q-separator
		q-tab-panels.col(v-model="tab" animated)
			q-tab-panel(name="view").row.row-gap
				q-card.resizable-content
					q-card-section
						q-btn(icon="visibility")
							q-menu
								q-item(v-for="col in columns" :key="col.label")
									q-item-section(side)
										q-checkbox
									q-item-section
										q-item-label {{col.label}}
						q-item(v-for="col in columns" :key="col.label")
							q-item-section
								q-item-label {{col.label}}
							q-item-section
								data-displayer(
									:row="row"
									:col="col"
									:date="date"
									)
				q-card.resizable-content
					q-card-section
						q-btn(icon="visibility")
							q-menu
								q-item(v-for="col in columns" :key="col.label")
									q-item-section(side)
										q-checkbox
									q-item-section
										q-item-label {{col.label}}
						q-item(v-for="col in columns" :key="col.label")
							q-item-section
								q-item-label {{col.label}}
							q-item-section
								data-displayer(
									:row="row"
									:col="col"
									:date="date"
									)
			q-tab-panel.q-pa-none(name="updates")
				
				div.q-py-lg
					q-item(v-for="item in 8" :key="item" dense)
						q-item-section(avatar)
							q-skeleton(type="QAvatar" size="36px")
						q-item-section
							q-item-label Task name
							q-item-label(caption) Juicy Smolliet
							
						q-item-section(side)
							div.row
								span.orgcombo-org 7
								span.orgcombo-role 5
						q-item-section(side)
							q-item-label(caption) 41 min
				q-card-actions
					q-btn(icon="refresh" flat)
					q-btn(icon="file_download" flat)
					q-pagination(
						style="margin-left: auto;"
						v-model="current"
						:max="10"
						:max-pages="6"
						boundary-numbers
						boundary-links
						color="grey-9"
						unelevated
						)
			q-tab-panel.q-pa-none(name="cycle")
				div.q-py-lg
					q-item(v-for="item in 8" :key="item" dense)
						q-item-section(avatar)
							q-skeleton(type="QAvatar" size="36px")
						q-item-section
							q-item-label Task name
							q-item-label(caption) Juicy Smolliet
							
						q-item-section(side)
							div.row
								span.orgcombo-org 7
								span.orgcombo-role 5
						q-item-section(side)
							q-item-label(caption) 41 min
				q-card-actions
					q-btn(icon="refresh" flat)
					q-btn(icon="file_download" flat)
					q-pagination(
						style="margin-left: auto;"
						v-model="current"
						:max="10"
						:max-pages="6"
						boundary-numbers
						boundary-links
						color="grey-9"
						unelevated
						)
			q-tab-panel.q-px-none.q-py-sm(name="approvals")
				div.q-py-lg
					template(v-for="item in 4" :key="item" dense)
						q-item.request-item
							q-item-section(side)
								div.task-selector
									div
										div
							q-item-section(avatar)
								q-skeleton(type="QAvatar" size="36px")
							q-item-section
								q-item-label Add $15,000 to Team X budget
								q-item-label Duration 1/1/2015 - 1/5/2019
								q-item-label(caption) Juicy Smolliet
							q-item-section(side)
								div.row
									q-btn(icon="assignment" round flat)
										q-tooltip
											div ACCEPT
									q-btn(icon="cancel" round flat)
										q-tooltip
											div REJECT
				q-card-actions
					q-btn(icon="refresh" flat)
					q-btn(icon="file_download" flat)
					q-pagination(
						style="margin-left: auto;"
						v-model="current"
						:max="10"
						:max-pages="6"
						boundary-numbers
						boundary-links
						color="grey-9"
						unelevated
						)
</template>

<script>
import dataDisplayer from './composition/data_displayer.vue'
export default {
	components: {
		dataDisplayer
	},
	props: ['row', 'columns', 'date'],
	data() {
			return {
				tab: 'updates',
				model: 'one',
				current: 3
			}
		}
	}
</script>

<style>
.q-item.request-item {
	padding: 5px 5px 5px 0!important;
}

.q-card {
	box-shadow: rgba(0, 0, 0, 0.1) -4px 9px 25px -6px;
}

.activity-menu {
	background: #757F9A;  /* fallback for old browsers */
	background: -webkit-linear-gradient(to right, #D7DDE8, #757F9A);  /* Chrome 10-25, Safari 5.1-6 */
	background: linear-gradient(to right, #D7DDE8, #757F9A); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

}


.resizable-content {
	min-height: 30px;
	min-width: 30px;
	resize: both;
	overflow: auto;
	max-height: fit-content;
	max-width: 300px;
}
</style>