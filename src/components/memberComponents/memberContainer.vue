<template lang="pug">
.right-scroll
  q-list.q-px-sm
    q-item MEMBER
    q-item.member-item(clickable v-for="member in members" :key="member")
      member-single-vue(:member="member[1]")

 
</template>

<script>
import memberSingleVue from "./memberSingle.vue";

export default {
  computed: {
    selected_serverdata() {
      return this.$store.state.serverdata.selected_serverdata;
    },
    selected_serverdata_roles() {
      return Object.entries(this.selected_serverdata.roles);
    },
    members() {
      return Object.entries(this.selected_serverdata.members)
    },
  },
  methods: {
    member(role) {
      console.log(role)
      return Object.entries(this.selected_serverdata.members).filter(
        (ele) => ele[1].roles.includes(role)
      );
    },
  },
  name: "MemberContainer",
  components: {
    memberSingleVue,
  },
};
</script>

<style scoped>
.right-scroll {
  background-color: #f2f3f5;
  width: 100%;
  height: 100%;
}

.member-item {
  padding: 10px 0;
}

</style>
