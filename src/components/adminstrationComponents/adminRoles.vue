<template>
  <h4>Roles</h4>
  <p>Use roles to blahblah.</p>
  <div class="cursor-pointer" @click="set_selected_menu">
    <h5>Default permissions</h5>
  </div>
  <q-btn label="Create role" />
  <q-table :rows="rows" :columns="columns" row-key="name"> </q-table>
</template>

<script>
export default {
  name: "AdminRoles",
  methods: {
    set_selected_menu() {
      this.$store.commit("set_admin_selected_menu", 'roles-detailed');
    },
  },
  data() {
    return {
      rows: [
        { roles: "JANITOR", members: 1 },
        { roles: "CHEF", members: 1 },
      ],
      columns: [
        { name: "roles", label: "ROLES", field: "roles" },
        { name: "members", label: "MEMBERS", field: "members" },
      ],
    };
  },
};
</script>

<style>
</style>