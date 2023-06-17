<template>
  <q-spinner
        color="primary"
        size="3em"
        :thickness="10"
      />
</template>

<script>
export default {
    sockets: {
        socket_init(data) {
            console.log(data)
            // this.$store.commit('mutate_socket_uid', data)
            this.fetch_init()
        },
        presence_update(data) {
            console.log(data)
        }
    },
    name: "InterstitialComponent",
    methods: {
        async fetch_init() {
            /*
            1. Fetch init data.
            2. If sxs, commit to store.
            3. If case: token expired, goto login.
            4. Route.
            */
            //1.
            await this.$api({
                method: 'get',
                url: '/init_data',
                headers : {
                    Authorization: `Bearer ${this.$store.state.auth}`
                }
            }).then((response)=>{
                //2.
                this.$store.commit('mutate_shallow', response.data);
                Object.entries(response.data).forEach(ele=>localStorage.setItem(ele[0], ele[1]))
                // 4.
                let state = this.$store.state.userdata.state
                state.selected_view == 'server' ? 
                    this.$router.push(`/channels/${state.selected_server}/${state.selected_room}`):
                    state.selected_view == 'friends' ? 
                    this.$router.push(`/channels/@me`):
                    state.selected_view == 'dm' ? 
                    this.$router.push(`/channels/@me/${state.selected_dm}`) :
                    this.$router.push(`/workspace/${state.selected_workspace}`)
                // document.addEventListener("visibilitychange", function logData() {
                //     if (document.visibilityState === "hidden") {
                //         navigator.sendBeacon("/window_close");
                //     }
                // });
            //3. 
            }).catch((error)=> {
                console.log(error)
                this.$router.push('/login');
            })
        }
    },
    async created() {
        /*
        1. Connect socket with auth.
        */
        //1.
        let auth = sessionStorage.getItem('jwt');
        this.$store.commit('mutate_auth', auth)
        this.$socket.client.auth.token = `Bearer ${auth}`;
        this.$socket.client.connect();
        if(localStorage.key(1) == null) this.fetch_init()
        else {
            this.$store.commit('mutate_shallow', {
                serverlist: localStorage.getItem('serverlist'),
                userdata: localStorage.getItem('userdata'),
                workspacedata: localStorage.getItem('workspacedata'),
                workspacelist: localStorage.getItem('workspacelist'),
            })
        }
        return
        this.$socket.client.on("error", (error) => {console.log(error)});
        this.$socket.client.on("connect_error", (error) => {
            console.log(`connect error: ${error}`);
            this.$router.push(`/login`)
            });
        this.$socket.client.on("disconnect", (reason) => { console.log(reason) });

        
    }
}
</script>

<style>

</style>