<template lang="pug">
q-list( separator)
  q-item
    q-item-section
      q-item-label {{userdata.username}} # {{userdata.discriminator}}
      q-item-label(caption lines="1") Username
    q-item-section(side)
      q-btn(icon="edit" round)
  q-item
    q-item-section
      q-item-label {{userdata.email}}
      q-item-label(caption lines="1") Email
    q-item-section(side)
      q-btn(icon="edit" round)
  q-item
    q-item-section(avatar)
      q-btn(icon="edit" color="deep-purple-12" unelevated) Edit password
  q-item
    q-item-section(avatar)
      q-btn(icon="edit" color="deep-purple-12" unelevated) Enable two-factor auth
  q-item
    q-item-section(avatar)
      q-btn(icon="edit" color="red" unelevated) Disable account
    q-item-section(avatar)
      q-btn(icon="edit" color="red" outline ) Delete account
</template>

<script>
export default {
    name: 'MyAccount',
    computed: {
      userdata() {
        return this.$store.state.userdata
      }
    }
}
</script>

<style>
</style>