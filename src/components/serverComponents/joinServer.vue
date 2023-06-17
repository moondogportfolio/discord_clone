<template lang="pug">
div(@click="isvisible_join_server_modal=true")
  slot(name="icon")
q-dialog(v-model="isvisible_join_server_modal")
  q-card.q-pa-sm
    q-card-section
      p.text-h6 Join Server
    q-input(outlined v-model="invite_id" label="invite id")
    q-card-actions
      q-btn(@click="join_server" color="blue") Join server
      q-btn(@click="isvisible_join_server_modal=false") Cancel

</template>

<script>
export default {
  data() {
    return {
      isvisible_join_server_modal: false,
      invite_id: null,
    }
  },
  methods: {
    join_server() {
      console.log('ENTER')
      this.$api({
        method: 'put',
        url: `/invite/${this.invite_id}`,
        headers : {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${this.$store.state.auth}`
         }
      }).then((response)=>{
        console.log(response.data);
      }).catch((error) => {
        null
      })
      this.isvisible_join_server_modal = false;
      this.invite_id = null
    }
  }
}
</script>

<style>

</style>