<template lang="pug">
q-dialog(v-model="isvisible_settings" persistent)
	q-card(style="width: 40vw; height: 40vh")
		q-card-section
			.row
				.col-shrink
					q-item(
						v-for="subfield in field"
						:key="subfield.label"
						@click="selected_field=subfield.type"
						clickable
						) {{subfield.label}}
				.col.q-pa-sm
					component(:is="selected_component")
		q-card-actions
			q-btn Save changes
			q-btn CANCEL
				
</template>

<script>
import numberSetting from './number.vue'
import textSetting from './text.vue'
import granularitySetting from './granularity.vue'
import statusSetting from './status.vue'
import groupSetting from './group.vue'
import tagSetting from './tag.vue'


var components = {
	'number': numberSetting,
	'text': textSetting,
	'granularity': granularitySetting,
	'status': statusSetting,
	'group': groupSetting,
	'tag': tagSetting
}

export default {
	props: ['field'],
	components: {
		numberSetting, textSetting, granularitySetting, groupSetting, statusSetting, tagSetting
		},
	computed: {
		selected_component() {
			return components[this.selected_field];
		}
	},
	data() {
		return {
			isvisible_settings: true,
			selected_field: 'status'
		}
	}
}
</script>

<style>

</style>