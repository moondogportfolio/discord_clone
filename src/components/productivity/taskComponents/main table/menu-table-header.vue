<template lang="pug">
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="settings")
	q-item-section
		q-item-label Settings
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="filter_alt")
	q-item-section
		q-item-label Filter
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="sort")
	q-item-section
		q-item-label Sort
q-separator
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="unfold_less")
	q-item-section
		q-item-label Collapse column
q-separator
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="drive_file_rename_outline")
	q-item-section
		q-item-label Rename
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="file_download")
	q-item-section
		q-item-label Export
	q-item-section(side)
		q-icon(size="24px" name="chevron_right")
q-separator
q-item(clickable)
	q-item-section(side)
		q-icon(size="24px" name="delete")
	q-item-section
		q-item-label Delete
</template>

<script>
export default {

}
</script>

<style>
.q-item {
	padding: 8px !important;
}
</style>