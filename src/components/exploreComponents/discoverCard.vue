<template lang="pug">
q-card.discover.q-ma-sm
    <q-img src="~/assets/mountains.jpg" ></q-img>
    q-card-section
        //- q-avatar(icon="settings")
        div.icon
        h6 {{server_partial.name}}
        p {{server_partial.description}}
    q-separator
    q-card-actions
        q-btn(@click="join_server") Join
  
</template>

<script>
export default {
    props: ["server_partial"],
    methods: {
        join_server() {
            this.$api({
                method: 'put',
                url: `/server/${this.server_partial._id}/members/${this.$store.state.userdata._id}`,
                headers : {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${this.$store.state.auth}`
                }
            }).then((response)=>{
                console.log(response)
            }).catch((error) => {
                null
            })
        }
    }
}
</script>

<style scoped>
.discover {
    width: 30%
}


.icon {
    height: 32px;
    width: 32px;
    background: black;
    border-radius: 5px;
    border: 3px solid green;
    position: absolute;
    top: 0px;
    left: 16px;
    transform: translateY(-50%);


}
</style>