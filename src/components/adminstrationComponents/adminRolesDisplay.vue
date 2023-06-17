<template>
  <q-input class="full-width" v-model="name" label="Role name"/>
  <div>
    <q-input
      filled
      v-model="color"
      :rules="['anyColor']"
      class="my-input"
      hint="Role Color"
    >
      <template v-slot:append>
        <q-icon name="colorize" class="cursor-pointer">
          <q-popup-proxy transition-show="scale" transition-hide="scale">
            <q-color v-model="color" />
          </q-popup-proxy>
        </q-icon>
      </template>
    </q-input>
    <div :style="get_style"></div>
    <q-toggle
      v-model="hoist"
      label="DISTINGUISH ROLE AND ONLINE MEMBERS"
    />
    <q-separator />
    <q-toggle v-model="mentionable" label="ALLOW @mention FOR ROLE" />

  </div>
</template>

<script>
import { mapFields } from 'vuex-map-fields';
export default {
  name: "AdminRolesDisplay",
  computed: {
    ...mapFields([
      'form_role.name',
      'form_role.color',
      'form_role.hoist',
      'form_role.mentionable',
    ]),
    get_style() {
      return `height: 50px; width: 50px; background: ${this.color}`;
    },
  },
};
</script>

<style>
</style>