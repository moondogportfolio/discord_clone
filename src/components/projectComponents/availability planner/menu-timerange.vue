<template lang="pug">
q-card-section.row
q-card-section.row
	q-input(label="From" outlined v-model="time" mask="time" :rules="['time']")
		template(v-slot:append)
			q-icon.cursor-pointer(name="access_time")
				q-menu
					q-time(v-model="time")
	div.col(style="width:20px")
	q-input(label="To" outlined v-model="time" mask="time" :rules="['time']")
		template(v-slot:append)
			q-icon.cursor-pointer(name="access_time")
				q-menu
					q-time(v-model="time")


q-card-section.position-relative
	span Add another entry
	q-btn.absolute-right.round-border(@click="$emit('update_cell',input_val)") Save
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
			time: '10:00',
      input_val: null
    }
  }

}
</script>

<style>

</style>