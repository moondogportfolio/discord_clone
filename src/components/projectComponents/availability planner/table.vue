<template lang="pug">
//- div.shadow-1.q-ma-sm
//- 	q-card-section
//- 	q-card-section.q-my-sm
//- 		div.row.q-my-sm(v-for="item in 10" :key="item")
//- 			div.col-shrink
//- 				q-skeleton(type="QAvatar")
//- 			div.col 16

q-table.shadow-1(
	:rows="rows"
	:columns="columns"
	row-key="name"
	)
	template(v-slot:header="props")
		q-tr
			q-th(v-for="col in props.cols" :key="col.fieldname")
				| {{ col.label }}
	template(v-slot:top="props")
		div.row.full-width.position-relative
			div.col-shrink.text-h5.q-mr-sm Working Times
			//- div.col.text-h5 Sep 12 - Sep 18, 2021
			div.col-shrink.absolute-right
				q-btn.q-ml-sm(icon="chevron_left" flat)
				q-btn.q-ml-sm(icon="calendar_today" flat)
				q-btn.q-ml-sm.round-border(icon="chevron_right" flat)
				q-btn(
          flat round dense
          :icon="props.inFullscreen ? 'fullscreen_exit' : 'fullscreen'"
          @click="props.toggleFullscreen"
					)
	template(v-slot:bottom)
		div.position-relative
			q-btn.absolute-bottom-left	(flat) + Availability rule
	template(v-slot:body="props")
		q-tr
			q-td.table-cell
				div
					|	{{ date.formatDate(props.row.start, 'MM/D/YY') }}
			q-td.table-cell
				div
					|	{{ date.formatDate(props.row.end, 'MM/D/YY') }}
			template(v-for="(col,index) in props.cols.slice(2, props.cols.length-1)" :key="col.fieldname")
				q-td.table-cell
					div {{ props.row?.[col.field].start }}
					div {{ props.row?.[col.field].end }}
					div {{ getHourDiff(props.row?.[col.field].start, props.row?.[col.field].end) }}
					q-menu
						menu-timerange
			q-td.table-cell
				div 5



</template>

<script>
import { date } from 'quasar';
import menuTimerange from './menu-timerange.vue'

export default {
	props: ["rows", "columns"],
	components: {
		menuTimerange
	},
	methods: {
		getHourDiff(start, end) {
			console.log(start, end);
			let parsed_start = date.extractDate(start, 'HH:mm')
			let parsed_end = date.extractDate(end, 'HH:mm')
			return date.getDateDiff(parsed_end, parsed_start, 'hours')
		}
	},
	created() {
			this.date = date
		},
}
</script>

<style>

.table-cell {
	white-space: normal;
	text-align:center
}

.delivered {
	border-left: 5px solid black;
}

.round-border-4 {
	border-radius: 0 0 0 10px;
}

.round-border-3 {
	border-radius: 0 0 10px 0;
}

.round-border-2 {
	border-radius: 0 10px 0 0;
}

.round-border-1 {
	border-radius: 10px 0 0 10;
}
</style>