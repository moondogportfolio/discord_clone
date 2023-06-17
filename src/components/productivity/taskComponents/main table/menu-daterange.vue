<template lang="pug">
q-date(
	v-model="input_val"
	today-btn
	:range="this.type=='daterange'"
  mask="YYYY-MM-DD"
	)
	q-btn(@click="validate") Set date
	div {{ input_val  }}
</template>

<script>
import {date} from 'quasar';
const {formatDate} = date;
export default {
  methods: {
    validate() {
      if(this.input_val != null) this.$emit('update_cell', this.input_val)
    }
  },
  created() {
		let now = formatDate( Date.now(), 'YYYY-MM-DD')
    this.input_val = this.type == 'daterange' ?
			this.value || {from:now, to: now} :
			this.value || now;
  },
  emits: ["update_cell"],
  props: ["value", "type"],
  data() {
    return {
      input_val: null
    }
  }

}
</script>

<style>

</style>