<template lang="pug">
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="highlight_off")
	q-item-section.q-ml-sm
		q-item-label Clear cell value
	q-item-section(side)
		q-icon(size="24px" name="backspace")
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="content_copy")
	q-item-section.q-ml-sm
		q-item-label Copy
	q-item-section(side) Ctrl + C
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="content_paste")
	q-item-section.q-ml-sm
		q-item-label Paste
	q-item-section(side) Ctrl + V
q-separator
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="message")
	q-item-section.q-ml-sm
		q-item-label Comment
q-separator
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="low_priority")
	q-item-section
		q-item-label Move to group
	q-item-section(side)
		q-icon(size="24px" name="chevron_right")
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="low_priority")
	q-item-section
		q-item-label Move to board
	q-item-section(side)
		q-icon(size="24px" name="chevron_right")
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="content_copy")
	q-item-section
		q-item-label Duplicate
	q-item-section(side)
		q-icon(size="24px" name="chevron_right")
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="add_circle_outline")
	q-item-section
		q-item-label Content copy
	q-item-section(side)
		q-icon(size="24px" name="chevron_right")
q-separator
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="horizontal_distribute")
	q-item-section
		q-item-label Distribute
	q-item-section(side)
		q-icon(size="24px" name="chevron_right")
	q-menu(anchor="center right" self="center left")
		menu-distribute

</template>

<script>
import menuDistribute from './menu-distribute.vue'
export default {
	components: {
		menuDistribute
	}

}
</script>

<style>

</style>