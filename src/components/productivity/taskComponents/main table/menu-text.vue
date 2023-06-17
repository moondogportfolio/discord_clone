<template lang="pug">
q-card-section.row
  q-input.col(v-model="input_val" outlined)
  q-btn.col-shrink.q-ml-sm(@click="$emit('update_cell', input_val)") OK
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
      edit_labels: false
    }
  }

}
</script>

<style>

</style>