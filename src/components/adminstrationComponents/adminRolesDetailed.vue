<template>
  <div class="row fit">
    <div class="col-4">
      <div class="relative-position">
        <q-btn label="Back" icon-right="arrow_back" @click="set_selected_menu"/>
        <q-btn icon="add" class="absolute-right" />
      </div>
      <div>
        <q-btn v-for="role in roles" :key="role" class="full-width">
          {{ role }}
        </q-btn>
      </div>
    </div>

    <div class="col relative-position fit">
      <template v-if="show_confirmation_banner">
        <div class="q-pa-md q-gutter-sm absolute-bottom" style="z-index: 1000">
          <q-banner inline-actions rounded class="bg-orange text-white">
            You have unsaved changes.

            <template v-slot:action>
              <q-btn flat label="Reset" @click="reset_permissions" />
              <q-btn flat label="Save Changes" @click="upload_permissions" />
            </template>
          </q-banner>
        </div>
      </template>
      <q-tabs
        v-model="edit_role_selected_tab"
        dense
        align="justify"
        narrow-indicator
      >
        <q-tab name="tab_display" label="Display" />
        <q-tab
          name="tab_permissions"
          label="Permissions"
          @click="update_serialized_permissions()"
        />
        <q-tab name="tab_manage_members" label="Manage Members" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="edit_role_selected_tab" animated>
        <q-tab-panel name="tab_display">
          <admin-roles-display></admin-roles-display>
        </q-tab-panel>
        <q-tab-panel name="tab_permissions">
          {{ serialized_permissions }}
          <template v-for="group in Object.keys(permissions)" :key="group">
            <h6>{{ group }}</h6>
            <template
              v-for="permission in permissions[group].permissions"
              :key="permission"
            >
              <div>
                <q-toggle
                  v-model="permission.value"
                  color="green"
                  @click="
                    (show_confirmation_banner = true),
                      update_serialized_permissions()
                  "
                  :label="permission.label"
                />
              </div>
            </template>
          </template>
        </q-tab-panel>
        <q-tab-panel name="tab_manage_members"> </q-tab-panel>
      </q-tab-panels>
    </div>
  </div>
</template>

<script>
import adminRolesDisplay from "./adminRolesDisplay.vue";
export default {
  components: { adminRolesDisplay },
  name: "RolesDetailed",
  computed: {
    serialized_permissions() {
      return this.$store.state.form_role.permissions
    }
  },
  methods: {
    set_selected_menu() {
      this.$store.commit('set_admin_selected_menu', 'roles')
    },
    update_serialized_permissions() {
      let x = 0;
      Object.keys(this.permissions).forEach((perm) => {
        this.permissions[perm].permissions.forEach((dictVal) => {
          dictVal.value ? (x = x ^ (1 << dictVal.bit)) : null;
        });
      });
      this.$store.commit('update_serialized_permissions', x);
    },
    upload_permissions() {
      this.show_confirmation_banner = false;
    },
    reset_permissions() {
      Object.keys(this.permissions).forEach((perm) => {
        this.permissions[perm].permissions.forEach((dictVal) => {
          dictVal.value = dictVal.value_orig;
        });
      });
      this.show_confirmation_banner = false;
    },
  },
  data() {
    return {
      show_confirmation_banner: false,
      edit_role_selected_tab: "tab_display",
      roles: ["JANITOR", "CHEF"],
      permissions: {
        general: {
          label: "General server permissions",
          permissions: [
            { label: "View channels", value: true, value_orig: true, bit: 10 },
            { label: "Manage channels", value: true, value_orig: true, bit: 4 },
            { label: "Manage roles", value: true, value_orig: true, bit: 28 },
          ],
        },
        membership: {
          label: "Membership permissions",
          permissions: [
            { label: "Create Invite", value: true, value_orig: true, bit: 0 },
            {
              label: "Change Nickname",
              value: true,
              value_orig: true,
              bit: 26,
            },
            {
              label: "Manage Nicknames",
              value: true,
              value_orig: true,
              bit: 27,
            },
          ],
        },
        textchannel: {
          label: "Text channel permissions",
          permissions: [
            { label: "Send Messages", value: true, value_orig: true, bit: 11 },
            { label: "Embed Links", value: true, value_orig: true, bit: 14 },
            { label: "Attach Files", value: true, value_orig: true, bit: 15 },
          ],
        },
      },
    };
  },
};
</script>

<style>
</style>