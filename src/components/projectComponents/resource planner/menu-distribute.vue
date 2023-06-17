<template lang="pug">
q-card
	q-card-section.distribute-header
		.distribute-top 10 day task
		.dist-label DISTRIBUTE
		.sched-label SCHEDULED
		.est-label ESTIMATE
		.dist-value
			q-input(bordered)
		.sched-value
			span 143 hrs
			span Clear time
		.est-value 144 hrs
	q-card-section
		div
			q-radio(v-model="loading_option" val="front" label="Front Load")
		div
			q-radio(v-model="loading_option" val="even" label="Distribute Evenly")
		div
			q-radio(v-model="loading_option" val="back" label="Back Load")
		div
			q-radio(v-model="loading_option" val="set" label="Consume set amount")
	q-card-actions
		q-btn(flat) Cancel
		q-btn Distribute
</template>

<script>
export default {
	data() {
		return {
			loading_option: 'front'
		}
	}
}
</script>

<style>
.distribute-header {
	display: grid;
	grid-template-rows: 1fr 15px 1fr;
	grid-template-columns: repeat(3, 1fr);
	grid-template-areas:
		"distribute-top . ."
		"dist-label sched-label est-label"
		"dist-value sched-value est-value ";
}

.distribute-top {
	grid-area: distribute-top;
}

.dist-label {
	grid-area: dist-label
}

.dist-value {
	grid-area: dist-value
}

.sched-label {
	grid-area: sched-label
}

.sched-value {
	grid-area: sched-value;
	text-align: center;
}

.est-label {
	grid-area: est-label
}

.est-value {
	grid-area: est-value
}

</style>