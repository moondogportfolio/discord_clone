<template lang="pug">
q-item
	q-item-section
		q-item-label Manage members
q-separator
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="manage_accounts" color="blue-grey-3")
	q-item-section
		q-item-label Manage members
	q-item-section(side)
		kbd Del
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="calendar_today")
	q-item-section
		q-item-label View schedules
	q-item-section(side)
		div.row
			kbd Ctrl
			span +
			kbd C
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="savings")
	q-item-section
		q-item-label View resources
	q-item-section(side)
		div.row
			kbd Ctrl
			span +
			kbd C
</template>

<script>
export default {
	emits: ['view_task_details'],
}
</script>

<style>

</style>