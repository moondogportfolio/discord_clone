<template lang="pug">
div.q-pa-sm.room
  q-expansion-item(
    expand-separator
    :model-value="open"
    switch-toggle-side
    :label-lines="1"
    :label="channel_data.name"
    dense
    )

    q-list(v-for="room in Object.entries(channel_data.rooms)", :key="room" dense)
      q-item(
        clickable
        v-ripple
        @click="set_selected_room(room[0])"
        )
        q-item-section
          q-item-label {{room[1].name}}
          q-item-label(caption v-if="selected_room==room[0]" side) SELECTED



</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  props: ["channel_data"],
  name: "ChannelChannel",
  computed: {
    ...mapState(["roomdata", "selected_room"]),
    selected_room() {
      return this.$store.state.userdata.state.selected_room
    }
  },
  methods: {
    ...mapMutations(["set_selected_room"]),
    set_selected_room(room) {
      
    },
    is_selected_room(room) {
      return this.$store.state.userdata.state.selected_room == room;
    },
  },
  data() {
    return {
      open: true,
      itemRefs: [],
    };
  },
  beforeUpdate() {
    this.itemRefs = [];
  },
  updated() {
    null;
  },
};
</script>
<style>
.room {
  color: #747f8d;
}

.selected_room {
  background-color: lightgray;
}
</style>
