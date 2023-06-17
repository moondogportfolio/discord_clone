import { boot } from 'quasar/wrappers'
import { io } from "socket.io-client";
import VueSocketIOExt from "vue-socket.io-extended";

const socket = io("http://127.0.0.1:8000/", {
  auth: {
    token: null
  },
  autoConnect: false
});

export default boot(({ app }) => {
  app.use(VueSocketIOExt, socket)
})
