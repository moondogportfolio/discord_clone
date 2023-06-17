<template lang="pug">
q-item(
  v-for="option in Object.entries(options)"
  :key="option[1].name"
  @click="$emit('update_cell', option[0])"
  clickable
  :class="`status-${option.name}`"
  )
  |	{{ option[1].name }}
q-separator
q-item(
  clickable
  @click="edit_labels=true"
  )
  | Add/edit label
</template>

<script>
export default {
  emits: ["update_cell"],
  props: ["options"],
  data() {
    return {
      edit_labels: false
    }
  }

}
</script>

<style>

</style>