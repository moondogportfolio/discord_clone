<template>
  <div class="fit column">
    <div class="col-shrink">
      <channel-header-vue></channel-header-vue>
    </div>
    <div class="col">
      <!-- <q-chip
        class="absolute-bottom"
        style="z-index: 1000"
        color="red"
        text-color="white"
      >
        NEW MENTIONS
      </q-chip> -->
      <q-scroll-area class="full-height">
        <template v-for="channel_data in channels_data" :key="channel_data">
          <channel-channel :channel_data="channel_data"></channel-channel>
        </template>
      </q-scroll-area>
    </div>
    <channel-card-vue ></channel-card-vue>
  </div>
</template>

<script>
import { mapState } from "vuex";
import channelCardVue from "./channelCard.vue";
import channelHeaderVue from "./channelHeader.vue";
import channelChannel from "./channelChannel.vue";

export default {
  name: "ChannelContainer",
  computed: {
    ...mapState(["selected_serverdata", "serverdata"]),
    channels_data() {
      try {
        return this.serverdata.selected_serverdata.channels;
      } catch {
        return 0;
      }
    },
  },
  components: {
    channelCardVue,
    channelChannel,
    channelHeaderVue,
  },
};
</script>

<style scoped>
</style>
