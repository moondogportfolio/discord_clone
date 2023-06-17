<template lang="pug">
div.q-pa-md.row(style="width:100%")
    template(v-for="server_partial in server_discover_partials" :key="server_partial")
        discover-card(:server_partial="server_partial")
</template>

<script>
import discoverCard from './discoverCard.vue'

export default {
    components: { discoverCard },
    name: "DiscoverMain",
    data() {
        return {
            server_discover_partials: null
        }
    },
    created() {
        this.$api({
            method: 'get',
            url: `/server/discover`,
        }).then((response)=>{
            console.log(response)
            this.server_discover_partials = response.data
        }).catch((error) => {
            null
        })
    
    }
}
</script>

<style>

</style>