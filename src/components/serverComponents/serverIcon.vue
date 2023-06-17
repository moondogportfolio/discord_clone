<template lang="pug">

div.relative-position.indicator-div-server.row.justify-center
  div.indicator-server.absolute-left
  q-avatar.server-icon.cursor-pointer.q-mt-sm(:id="server_name", size="40px" :icon="icon" :color="color")
    template(v-if="server_id")
      q-img(:src="`http://localhost:8000/server-icon/${server_id}`")
    q-badge(rounded, color="red", floating)
  server-tooltip-vue.bg-amber.text-black(:server="server_name")
</template>

<script>
import serverMenuVue from "./serverMenu.vue";
import serverTooltipVue from "./serverTooltip.vue";

export default {
  props: ["server_id", "server_name", "icon", "color"],
  name: "ServerIcon",
  components: {
    serverMenuVue,
    serverTooltipVue,
  }
};
</script>

<style>
.indicator-server {
  margin: auto 0;
  width: 6px;
  height: 10px;
  border-radius: 0 5px 5px 0;
  background-color: black;
  transition: height 0.2s ease-out;
}


.indicator-div-server:hover .indicator-server {
  width: 6px;
  height: 20px;
}

.indicator-div-server:hover .server-icon {
  border-radius: 40%;
}

.indicator-settings {
  margin: auto 0;
  width: 6px;
  height: 10px;
  visibility: hidden;
  border-radius: 0 5px 5px 0;
  background-color: black;
}

.indicator-div-settings:hover .indicator-settings {
  visibility: visible;
  transition: height 0.2s ease-out;
  height: 20px;
}

.indicator-div-settings:hover .server-icon {
  border-radius: 40%;
}


.server-icon {
  transition: border-radius 0.2s ease-out;
}

</style>
