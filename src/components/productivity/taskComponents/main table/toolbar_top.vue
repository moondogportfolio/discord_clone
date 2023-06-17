<template lang="pug">
q-card.q-ma-sm.row
	q-btn-group
		q-btn(unelevated ) New Item
		q-btn-dropdown(color="grey-5")
	q-item(clickable)
		q-item-section(side)
			q-icon(name="filter_alt")
		q-item-section
			q-item-label Filter
	q-item(clickable)
		q-item-section(side)
			q-icon(name="sort")
		q-item-section
			q-item-label Sort
	q-item(clickable)
		q-item-section(side)
			q-icon(name="push_pin")
		q-item-section
			q-item-label /6
	q-item(clickable)
		q-item-section(side)
			q-icon(name="visibility_off")
		q-item-section
			q-item-label /6
	q-item(clickable)
		q-item-section(side)
			q-icon(name="height")
	q-item(clickable)
		q-item-section(side)
			q-icon(name="format_color_fill")
	q-item(clickable)
		q-item-section(side)
			q-icon(name="drive_file_rename_outline")
	.col-shrink
</template>

<script>

export default {
};
</script>

<style scoped>
.header-bar {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
  height: 48px;
  padding: 12px 0;
}
</style>
