<template lang="pug">
q-card
	q-item(v-for="item in Object.entries(checkboxes)" :key="item[0]")
		q-item-section
			q-item-label {{ item[0] }}
		q-item-section(side)
			q-checkbox(
				@click="update_checkbox(item[0], checkboxes[item[0]])"
				v-model="checkboxes[item[0]]"
				)
		q-item-section(side)
			q-btn(icon="remove" @click="" round size="xs")
	q-item
		q-item-section
			q-input(outlined dense v-model="input_val")
		q-item-section(side)
			q-btn(@click="create_checkbox") Add
		
</template>

<script>
export default {
	created() {
		this.checkboxes = _.cloneDeep(this.value)
	},
	methods: {
		update_checkbox(checkbox_name, checkbox_value) {
			this.$emit('add_value_subvalue', {[checkbox_name]: checkbox_value})
		},
		create_checkbox() {
			this.$emit('add_value_subvalue', {[this.input_val]: false})
			this.checkboxes[this.input_val] = false
			this.input_val = null

		}
	},
	props: ['value'],
	emits: ['update_cell', 'add_value_subvalue'],
	data() {
		return {
			checkboxes: null,
			input_val: null
		}
	}
}
</script>

<style>

</style>