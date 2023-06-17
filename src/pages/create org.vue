<template lang="pug">
q-card.absolute-center(style="width: 60vw; height:80vh")
	q-card-section.column.fit.q-pa-none
		q-tabs.col-shrink(
			v-model="tab"
			class="text-grey"
			active-color="primary"
			inline-label
			indicator-color="primary"
			align="justify"
			narrow-indicator
		)
			div.row.q-ml-sm.row-gap
				q-btn(icon="visibility" @click.prevent="" round)
				q-btn(icon="compare" @click.prevent="" round)
			q-tab(name="group" label="Group Settings")
			q-tab(name="add" label="Add Member")
			q-tab(name="edit" label="Edit Settings")
			
		q-separator
		q-tab-panels.col(v-model="tab" animated)
			q-tab-panel(name="add")

				q-item(v-for="item in 3" :key="item")
					q-item-section(avatar)
						q-skeleton(type="QAvatar")
					q-item-section
						q-item-label.ellipsis James Fallon Lembert II
					q-item-section
						q-item-label Manager
				q-input(outlined dense placeholder="Add member")
					template(v-slot:append)
						q-btn(icon="add" flat dense)
				q-item(v-for="item in 2" :key="item" clickable)
					q-item-section(avatar)
						q-skeleton(type="QAvatar")
					q-item-section
						q-item-label Name
					q-item-section(side)
						div.row
							div(v-for="chip in 3" :key="chip")
								span.orgcombo-org Joy Division
								span.orgcombo-role Manager
			q-tab-panel(name="edit")
				q-item(v-for="item in 16" :key="item")
					q-item-section(avatar)
						q-skeleton(type="QAvatar")
					q-item-section
						q-item-label Name
					q-item-section(side)
						div.row-gap.row
							q-btn(icon="assignment" round flat)
							q-btn(icon="assignment" round flat)
							q-btn(icon="assignment" round)
</template>

<script>
export default {
	data() {
		return {
			tab: 'add',
			model: 'one'
		}
	}
}
</script>

<style>

</style>