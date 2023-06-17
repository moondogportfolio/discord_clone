<template lang="pug">
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="settings")
	q-item-section
		q-item-label Task Settings
q-separator
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="low_priority")
	q-item-section
		q-item-label Move to group
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="chevron_right")
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="low_priority")
	q-item-section
		q-item-label Move to board
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="chevron_right")
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="content_copy")
	q-item-section
		q-item-label Duplicate
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="chevron_right")
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="add_circle_outline")
	q-item-section
		q-item-label Content copy
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="chevron_right")
q-separator
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="delete")
	q-item-section
		q-item-label Delete
</template>

<script>
export default {
	emits: ['view_task_details'],
	components: {
	}
}
</script>

<style>

</style>