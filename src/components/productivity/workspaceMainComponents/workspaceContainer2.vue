<template lang="pug">
q-card-section.column.fit.q-pa-none
	q-tabs.col-shrink.wenk(
		dense
		v-model="tab"
		class="text-grey"
		indicator-color="transparent"
		active-color="black"
		align="justify"
		no-caps
	)
		q-tab(name="activity" label="Activity")
		q-tab(name="boards" label="Boards")
		q-tab(name="gantt" label="Gantt")
		q-tab(name="resources" label="Resources")
		q-tab(name="people" label="People")
	q-separator
	q-tab-panels.col(v-model="tab")
		q-tab-panel(name="activity")
		q-tab-panel(name="boards")
		q-tab-panel(name="gantt")
		q-tab-panel(name="resources")
		q-tab-panel(name="people")
		
</template>

<script>
export default {
data() {
		return {
			tab: 'activity',
			model: 'one'
		}
	}
}
</script>

<style>
.wenk {
	background: #F2F3F5;
}
</style>