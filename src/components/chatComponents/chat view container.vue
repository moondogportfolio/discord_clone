<template lang="pug">
.chat-container.q-ma-sm.full-height
  .area-a.row
    //- template(v-for="room_id in pinned_rooms" :key="room_id")
    //-   chat-box(
    //-     v-if="selected_room != room_id"
    //-     :post_entries="Object.entries(roomdata[room_id].posts)"
    //-     :room_id="room_id"
    //-     :ispinned="true")
    template(v-if="selected_room") 
      chat-box(:post_entries="Object.entries(selected_roomdata.posts)" :room_id="selected_room" :ispinned="false")
    //- q-spinner-grid.absolute-center(v-else color="primary" size="2em")
  .main-input
    chat-input-vue


</template>

<script>
import chatInputVue from "./chatInputContainer.vue";
import chatBox from './single chat box.vue';
import { ref } from 'vue';
import { mapState,mapGetters } from 'vuex'

export default {
  props: ["post_entries"],
  computed: {
    ...mapState(['roomdata', 'selected_room']),
    ...mapGetters(['pinned_rooms', 'selected_roomdata']),
  },
  components: {
    chatInputVue,
    chatBox,
  },
  name: "ChatContainer",
};
</script>

<style>

.is-selected {
  border: 1px solid red !important;
}

.chat-container {
  display: grid;
  gap: 2px 2px;
  grid-template-rows: 1fr auto;
  grid-template-columns: auto;
  grid-template-areas: 
    "chat" 
    "input";
} 

.area-a {
  grid-area: chat;
}

.area-a .column {
  border:1px solid lightgray;
  margin: 2px;
}

.area-a .column .row {
  background: blanchedalmond;
}

.b {
  border:1px solid lightgray;
  grid-area: chat2;
}

.c {
  border:1px solid lightgray;
  grid-area: chat3;
}

.d {
  border:1px solid lightgray;
  grid-area: chat4;
  place-self: center;
}

.main-input {
  grid-area: input;
}



</style>
