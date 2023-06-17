<template>
  <canvas id="canvas"></canvas>

  <!-- <socket-vue></socket-vue> -->
  <firstpage-container></firstpage-container>
  <!-- <main-view v-else></main-view> -->
</template>

<script>
// import socketVue from "components/connectivityComponents/socket.vue";
import FirstpageContainer from "components/firstpageComponents/firstpageContainer.vue";
// import MainView from './MainView.vue';
import { defineComponent } from 'vue';

// import { defineAsyncComponent } from "vue";
// const AppPostLogin = defineAsyncComponent(
//   () => import("./AppPostLogin.vue")
// );

export default defineComponent({
  name: "FirstView",
  components: {
    // socketVue,
    FirstpageContainer,
    // MainView,
  },
  created() {
    document.addEventListener("visibilitychange", function logData() {
      if (document.visibilityState === "hidden") {
        navigator.sendBeacon("/window_close");
      }
    });
  },
});
</script>

<style lang="sass">
</style>
