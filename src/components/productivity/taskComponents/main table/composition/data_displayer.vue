<template lang="pug">

template(v-if="col.type=='checkbox'")
	div ✅: {{ checkbox_props(row?.[col.fieldname], true) }}
	div ❌: {{ checkbox_props(row?.[col.fieldname], false) }}
	div {{ row?.[col.fieldname] }}
	//- q-checkbox(v-model="checkbox_temp[col.fieldname]")
template(v-else-if="row?.[col.fieldname]!=null")
	template(v-if="col.fieldname=='group'")
		q-chip(v-for="group in row?.[col.fieldname]" :key="group") {{ group }}
	template(v-else-if="col.type=='daterange' && row?.[col.fieldname]!= null")
		div.text-white.q-pa-xs(:style="schedule_bar(row?.[col.fieldname])")
			| {{ date.formatDate(row?.[col.fieldname].from, 'MMM D -') }}
			| {{ date.formatDate(row?.[col.fieldname].to, 'MMM D') }}
	div(v-else-if="col.type=='date'")
		|	{{ date.formatDate(row?.[col.fieldname], 'MMM D') }}
	div(v-else)
		|	{{ row?.[col.fieldname] }}
	//- | {{ props.cols[index].type }}
div.text-grey(v-else) ∅
</template>

<script>
export default {
	props: ["col", "row", "date"],
	methods: {
		schedule_bar(date) {
			let from_diff =  this.date.getDateDiff(date.from, Date.now(), 'days')
			let to_diff =  this.date.getDateDiff(date.to, Date.now(), 'days')
			if(from_diff < 0 && to_diff < 0) return `background: black;`
			else if(from_diff > 0 && to_diff > 0) return `background: blue;`
			else {
				let first_stop = `${Math.trunc((-from_diff/(-from_diff+to_diff))*100)}%`
				return `background: linear-gradient(to right, rgb(102, 204, 255) ${first_stop}, rgb(28, 31, 59) ${first_stop});`
			}
		},
	}
}
</script>

<style>

</style>