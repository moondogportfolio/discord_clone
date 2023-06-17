<template lang="pug">
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="unfold_less")
	q-item-section
		q-item-label Collapse this board
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="unfold_less")
	q-item-section
		q-item-label Collapse all boards
	q-item-section(side)
		div.row
			kbd Ctrl
			span +
			kbd B
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="check_box")
	q-item-section
		q-item-label Select all tasks
q-separator
q-item(clickable dense @click="$emit('add_task_dialog')")
	q-item-section(side)
		q-icon(size="24px" name="add_circle_outline")
	q-item-section
		q-item-label Add task
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="add_circle_outline")
	q-item-section
		q-item-label Create field	
	q-item-section(side)
		q-icon(size="24px" name="chevron_right")
	q-menu(anchor="top right" self="top left")
		menu-create-field(:board_id="board_id")
q-separator
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="low_priority")
	q-item-section
		q-item-label Move to workspace
	q-item-section(side)
		q-icon(size="24px" name="chevron_right")
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="low_priority")
	q-item-section
		q-item-label Move to group
	q-item-section(side)
		q-icon(size="24px" name="chevron_right")
q-separator
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="drive_file_rename_outline")
	q-item-section
		q-item-label Rename
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue" tag="span" style="background:blue")
	q-item-section
		q-item-label Change board color
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="file_download")
	q-item-section
		q-item-label Export
	q-item-section(side)
		q-icon(size="24px" name="chevron_right")
q-separator
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="delete")
	q-item-section
		q-item-label Delete
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="archive")
	q-item-section
		q-item-label Archive

</template>

<script>
import menuCreateField from './menu-create-field.vue'
export default {
	props: ['board_id'],
	emits: ['add_task_dialog'],
	components: {
		menuCreateField
	}
}
</script>

<style>
.q-item {
	padding: 8px !important;
}
</style>