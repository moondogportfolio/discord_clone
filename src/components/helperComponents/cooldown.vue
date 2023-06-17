<template>
  <input type="text" v-model="inputdata" @keyup.enter="send" />
  <div>{{ sent_chat }}</div>
  <p>{{ timer }}</p>
</template>

<script>
export default {
  name: "cooldown",
  data() {
    return {
      inputdata: null,
      sent_chat: [],
      timer: 0,
      cooldown: 5,
      timerObj: null,
    };
  },
  methods: {
    send() {
      if (this.timer == 0) {
        let timerFunc = () => {
            console.log(this.timer);
            this.timer--;
            this.timer == 0 ? clearInterval(this.timerObj) : null
        }
        this.sent_chat.push(this.inputdata);
        this.inputdata = null;
        this.timer = this.cooldown;
        this.timerObj = setInterval(timerFunc, 1000)
      }
    },
  },
};
</script>

<style>
</style>