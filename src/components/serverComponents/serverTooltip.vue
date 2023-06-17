<template>
  <!-- <q-tooltip anchor="center right" :target="'#' + target" self="center left"> -->
  <q-tooltip anchor="center right" self="center left">

    <div class="tooltip">{{ server }}</div>
  </q-tooltip>
</template>

<script>
export default {
  props: ["server"],
  name: "ServerTooltip",
};
</script>

<style>
.tooltip {
  font-size: 15px;
}
</style>
