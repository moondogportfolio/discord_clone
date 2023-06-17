<template>
  <div class="fit column">
    <div class="col-shrink">
      <dm-container-header></dm-container-header>
    </div>
    <div class="col relative-position q-pa-sm">
      <friend-panel-friends></friend-panel-friends>
    </div>
    <channel-card-vue class="col-shrink"></channel-card-vue>
  </div>
</template>

<script>
import channelCardVue from "../channelComponents/channelCard.vue";
import DmContainerHeader from './dmContainerHeader.vue';
import friendPanelFriends from "./friendPanelFriends.vue";

export default {
  components: { friendPanelFriends,channelCardVue, DmContainerHeader },
  name: "FriendPanelContainer",
};
</script>

<style>
</style>