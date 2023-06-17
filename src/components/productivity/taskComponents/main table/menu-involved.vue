<template lang="pug">
q-card
  q-card-section
  q-card-section
    div(v-for="item in 10" :key="item")
      q-skeleton(type="circle")
      div 16
</template>

<script>
export default {

}
</script>

<style>

</style>