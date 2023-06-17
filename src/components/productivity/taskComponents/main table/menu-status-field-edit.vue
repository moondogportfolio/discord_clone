<template lang="pug">
q-item(
  v-for="option in options"
  :key="option.name"
  @click="$emit('update_cell', option.name)"
  :class="`status-${option.name}`"
  )
  q-item-section(side)
    q-btn(:style="`background: ${option.color}`" round size="6px")
      q-menu( transition-show="scale")
        q-color(v-model="color_input" no-header)
  q-item-section
    q-item-label {{ option.name }}
  q-item-section(side)
    q-btn(icon="close" round size="6px")
  
q-item
  q-item-section
      q-btn(icon="add" size="12px" unelevated)
q-btn.full-width APPLY
</template>

<script>
export default {
  emits: ["update_cell"],
  props: ["options"],
  data() {
    return {
      edit_labels: false,
      color_input: null,
    }
  }

}
</script>

<style>

</style>