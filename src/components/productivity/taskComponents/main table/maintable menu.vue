<template lang="pug">
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" name="highlight_off" color="blue-grey-3")
	q-item-section
		q-item-label Clear cell value
	q-item-section(side)
		kbd Del
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="content_copy")
	q-item-section
		q-item-label Copy
	q-item-section(side)
		div.row
			kbd Ctrl
			span +
			kbd C
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="content_paste")
	q-item-section
		q-item-label Paste
	q-item-section(side)
		div.row
			kbd Ctrl
			span +
			kbd V
q-separator
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="message")
	q-item-section
		q-item-label Comment
q-item(clickable dense @click="$emit('view_task_details')")
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="expand_more")
	q-item-section
		q-item-label View Task
q-separator
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="flip_to_front")
	q-item-section
		q-item-label Convert to Reference
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="chevron_right")
	q-menu(anchor="center right" self="center left")
		menu-ref-mirror
		
q-item(clickable dense)
	q-item-section(side)
		q-icon(size="24px" color="blue-grey-3"  name="swap_horizontal_circle")
	q-item-section
		q-item-label Convert to Mirror
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
import menuRefMirror from './menu/menu-ref-mirror.vue'
export default {
	emits: ['view_task_details'],
	components: {
		menuRefMirror,
	}
}
</script>

<style>

</style>