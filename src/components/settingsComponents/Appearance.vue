<template lang="pug">
q-card(flat)
  q-card-section
    p.text-h5 Appearance
    div.example.bordered
  q-separator(inset)
  q-card-section
    p THEME
    q-list.q-pa-none
      q-item.q-px-none
        q-radio.full-width.bordered.q-pa-sm(v-model="theme" val="light" label="Light")
      q-item.q-px-none
        q-radio.full-width.bordered.q-pa-sm(v-model="theme" val="dark" label="Dark")
      q-item.q-px-none
        q-toggle(v-model="dark_sidebar" label="Dark Sidebar" left-label)
  q-card-section
    p MESSAGE DISPLAY
    q-list.q-pa-none
      q-item.q-px-none
        q-radio.full-width.bordered.q-pa-sm(v-model="message_display" val="cozy" label="Cozy")
      q-item.q-px-none
        q-radio.full-width.bordered.q-pa-sm(v-model="message_display" val="compact" label="Compact")
</template>

<script>
export default {
  data() {
    return {
      theme: 'light',
      dark_sidebar: false,
      message_display: 'cozy'
    }
  }
}
</script>

<style scoped>
.example {
  width: 100%;
  height: 20vh;
}

.bordered {
  border: 1px solid lightgray;
  border-radius: 5px;
}
</style>