<template lang="pug">
.column.col(:data-room-id="room_id" :class="isselected_room" @click="set_focused_room")
  .row.justify-end.col-shrink.q-pa-sm
    span {{ room_id }}
    q-icon.cursor-pointer(
      name="push_pin"
      size="16px"
      @click="remember_pinned_chat"
      :color="ispinned? 'black': 'grey'"
      )
    q-icon.cursor-pointer(name="close" size="16px")
  q-scroll-area.col(ref="chatContainerScrollRef" @scroll="scroll_update")
    template(v-for="post in post_entries" :key="post[0]")
      chat-singlechat-vue(       
        :post="post[1]"
        :post_id="post[0]"
        :chatContainerScrollRef = "chatContainerScrollRef"
        :reference="null")



</template>

<script>
import chatSinglechatVue from "./chatSinglechat.vue";
import { ref } from 'vue'
import { mapState,mapGetters } from 'vuex'

export default {
  props: ["post_entries", "room_id", "ispinned"],
  computed: {
    ...mapState(['focused_room']),
    ...mapGetters(['pinned_rooms']),
    isselected_room() {
      return this.room_id == this.focused_room ? 'is-selected' : null
    }
  },
  methods: {
    set_focused_room() {
      if(this.focused_room != this.room_id) this.$store.commit('mutate_deep', {
				focused_room: this.room_id})
    },
    remember_pinned_chat() {
      let pinned_rooms = this.ispinned ?
        this.pinned_rooms.filter(ele=>ele!=this.room_id) :
        this.pinned_rooms.concat(this.room_id)
      this.$store.commit('mutate_deep_arrayset',
          {
            userdata: { state: {pinned_rooms: pinned_rooms }},
            selected_room: !this.ispinned ? null: this.room_id
          }
        );
      return
      this.$api({
        method: 'patch',
        url: '/users/@me',
        data: {
            state: {
              pinned_rooms: [this.room_id]
            }
        },
        headers : {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.$store.state.auth}`
         }
      }).then((response)=>{
      }).catch((error) => {
        console.log(error)
      })
    },
    scroll_update(info) {
      if (info.verticalSize>this.scroll_size) {
        this.scroll_size = info.verticalSize;
        info.ref.setScrollPercentage('vertical', 1, 0)
      }

    }
  },
  setup() {
    const chatContainerScrollRef = ref(null)
    var scroll_size = ref(0)
    return {
      chatContainerScrollRef,
      scroll_size
    }
  },
  components: {
    chatSinglechatVue,
  },
  name: "ChatContainer",
};
</script>

<style>



</style>
