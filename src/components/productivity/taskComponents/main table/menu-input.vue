<template lang="pug">
q-card-section.row
  q-input.col(v-model="input_val" outlined)
    template(v-slot:append)
      q-btn.col-shrink.q-ml-sm(@click="cast_to_int" icon="add" dense)
</template>

<script>
export default {
  created() {
    this.input_val = this.value;
  },
  methods: {
    cast_to_int() {
      this.$emit('update_cell', this.type == 'number' ? Number(this.input_val): this.input_val)
    },
  },
  emits: ["update_cell"],
  props: ["value", "type"],
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