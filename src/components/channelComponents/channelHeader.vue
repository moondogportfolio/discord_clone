<template lang="pug">
//- img.full-width(src='~/assets/mountains.jpg' style="height: 10vh")
div.header-div
  channel-header-menu-vue
</template>

<script>
import channelHeaderMenuVue from "./channelHeaderMenu.vue";

export default {
  components: {
    channelHeaderMenuVue,
  },
  name: "ChannelHeader",
};
</script>

<style scoped>
.header-div {
  height: 20vh;
  width: 100%;
  background: black;
  border-radius: 10px 0 0 0;
}
</style>
