<template lang="pug">
q-card(style="width:40vw; max-height:500px")
	q-card-section
		q-input(outlined type="textarea")
	q-card-section.row
		div.col.q-mr-md
			q-expansion-item(
				expand-separator
				label="Account settings"
				type="textarea"
				)
				q-item AW
				q-item aw
				q-item AW
				q-item aw
				q-item AW
				q-item aw
				q-item AW
				q-item aw
		div.col-8
			div.text-h6 MIN
			div Returns the bullshit explanation.
			div.text-h6 Examples
			div MIN(1,2,3,4,5)
	q-card-actions.row
		q-icon(name="help_outline")
		span.text-grey Learn more about formulas
		q-btn.set-formula Set formula

</template>

<script>
export default {

}
</script>

<style>

.set-formula {
	margin-left: auto
}
</style>