<template lang="pug">
q-card-section(style="width: 30vw")
  q-slider(
    v-model="input_val"
    :step="1"
    :min="0"
    :max="type=='progress'?100:10"
    label
    label-always
    )
  q-btn.q-ml-sm(@click="$emit('update_cell', input_val)") SET
  span Settings - Step:1 Min:0 Max:10
</template>

<script>
export default {
  created() {
    this.input_val = this.value;
  },
  emits: ["update_cell"],
  props: ["value", "type"],
  data() {
    return {
      input_val: 1,
      edit_labels: false
    }
  }

}
</script>

<style>

</style>