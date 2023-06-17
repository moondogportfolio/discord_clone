<template lang="pug">
q-card
	q-color(
		v-model="input_val"
		no-header
		)
	q-btn(@click="$emit('update_cell', input_val)") OK
</template>

<script>
export default {
	created() {
		this.input_val = this.value;
	},
	emits: ["update_cell"],
	props: ["value"],
	data() {
		return {
			input_val: null,
		}
	}

}
</script>

<style>

</style>