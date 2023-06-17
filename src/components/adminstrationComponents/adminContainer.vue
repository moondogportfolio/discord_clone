<template>
  <div class="row">
    <div class="col-4">
      <q-list>
        <q-item
          v-for="menu in menus"
          :key="menu"
          clickable
          v-ripple
          @click="set_selected_menu(menu)"
        >
          {{ menu }}
        </q-item>
      </q-list>
    </div>
    <div class="col window-height">
      <q-tab-panels v-model="selected_menu" class="fit">
        <q-tab-panel name="overview">
            <admin-overview-vue></admin-overview-vue>
        </q-tab-panel>
        <q-tab-panel name="roles">
            <admin-roles-vue></admin-roles-vue>
        </q-tab-panel>
        <q-tab-panel name="emoji">
            <admin-emoji-vue></admin-emoji-vue>
        </q-tab-panel>
        <q-tab-panel name="roles-detailed">
            <admin-roles-detailed-vue></admin-roles-detailed-vue>
        </q-tab-panel>
      </q-tab-panels>
    </div>
  </div>
</template>

<script>
import adminEmojiVue from "./adminEmoji.vue";
import adminOverviewVue from "./adminOverview.vue";
import adminRolesVue from "./adminRoles.vue";
import adminRolesDetailedVue from './adminRolesDetailed.vue';


export default {
  name: 'AdminContainer',
  components: {
    adminOverviewVue,
    adminEmojiVue,
    adminRolesVue,
    adminRolesDetailedVue,
  },
  computed: {
      selected_menu() {
          return this.$store.state.admin_selected_menu
      }
  },
  methods: {
    set_selected_menu(menu) {
      this.$store.commit('set_admin_selected_menu', menu)
    },
  },
  data() {
    return {
      menus: ["overview", "roles", "emoji"],
    };
  },
};
</script>

<style>
</style>