<template>
<img src="~/assets/orchid.png" class="orchid"/>

  <canvas id="canvas"></canvas>
  <div class="row">
    <div class="shadow-1 col-4 fixed-center">
      <q-tabs
        v-model="tab"
        dense
        class="bg-grey-3"
        align="justify"
        narrow-indicator
      >
        <q-tab name="register" label="Register" />
        <q-tab name="login" label="Login" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="register">
          <register></register>
        </q-tab-panel>
        <q-tab-panel name="login">
          <login></login>
          
        </q-tab-panel>
      </q-tab-panels>
    </div>
  </div>
</template>

<script>

import register from "../firstpageComponents/register.vue";
import Login from "../firstpageComponents/login.vue";



export default {
  components: { register, Login },
    computed: {
      daym() {
        return this.$store.state.data
      }
    },
  data() {
    return {
      tab: "login",
    };
  },
  name: "FirstPageContainer",
};
</script>

<style>
.orchid {
  position: absolute;
  left:0;
  height: 80%;
  width: auto;
  bottom: 200px;
}
</style>