<template lang="pug">
div.full-height(style="background:#F2F3F5")
  //- q-item(v-for="participant in participants" :key="participant")
  //-   q-item-section(avatar)
  //-     q-img(:src="`http://localhost:8000/user-icon/${participant._id}`")  
  //-   q-item-section
  //-     q-item-label {{participant.nick}}

</template>

<script>
export default {
    name: 'dm_participants',
    computed: {
      participants() {
        return this.$store.getters.selected_roomdata.participants
      }
    }
}
</script>

<style>

</style>