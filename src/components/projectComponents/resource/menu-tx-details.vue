<template lang="pug">
q-item
	q-item-section
		q-select(label="Status" v-model="details.status" dense)
	q-item-section
		q-input(label="Date" dense v-model="details.initiation_date")
q-item
	q-item-section
		q-input(label="Description" dense v-model="details.description")
q-item
	q-item-section
		q-input(label="Initiator" dense v-model="details.initiation")
q-item
	q-item-section
		q-input(label="Approval" dense v-model="details.approval")
</template>

<script>

export default {
	props: ['details']
}
</script>

<style>

</style>
