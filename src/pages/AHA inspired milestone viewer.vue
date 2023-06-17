<template lang="pug">
q-btn(@click="isvisible_details=!isvisible_details") switch
div(style="overflow: auto; width: max-content")
  div.row
    div.column.col.release(v-for="a in 5" :key="a")
      div title
      div.feature.q-ma-sm(
        v-for="a in 5"
        :key="a"
        @click="isvisible_details=!isvisible_details"
        ) wee
        div DEMOIT-16
        div Chart plugin
        div In progress

div.details(v-if="isvisible_details")

</template>

<script>
export default {
  data() {
    return {
      isvisible_details: false
    }
  }
}
</script>

<style>
.feature {
  border: 1px burlywood solid;
  border-radius: 5px;
  border-left: 5px burlywood solid;
}

.release {
  min-width: 300px !important;
}

.details {
  position: absolute;
  right:0;
  top:0;
  width: 300px;
  height: 100%;
  background: blanchedalmond;
}
</style>