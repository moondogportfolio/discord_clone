<template lang="pug">
q-btn.search(label="Find or start a conversation" @click="alert = true" color="grey-4" unelevated no-caps)
q-dialog(v-model="alert")
  q-card
    q-card-section
      q-input.shadow-6

</template>

<script>
export default {
    name: "FriendPanelHeader",
    data() {
      return {
        alert: false
      }
    }
}
</script>

<style scoped>
.search {
  display: block;
  margin: auto;
  margin-top: 10px;
}
</style>