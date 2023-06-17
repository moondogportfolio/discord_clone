<template lang="pug">



.emoticon-container.rborder.shadow-1.column
  .col-shrink.full-width(style='border-bottom: 1px solid lightgray')
    q-tabs(
      v-model="emoticon_category"
      dense
      class="text-grey"
      active-color="primary"
      indicator-color="primary"
      align="justify"
      narrow-indicator
      )
      q-tab(name="gif" label="GIFs")
      q-tab(name="sticker" label="Stickers")
      q-tab(name="emoji" label="Emoji")
    q-input.q-ma-sm(outlined dense v-model="emoticon_search" )
      template(v-slot:append)
        q-icon(name="add_box")
  .row.col.fit 
    .col-shrink(style='background: #E3E5E8; overflow: hidden')
      div(v-for='folder in folders', :key='folder', @click='scroll_into_view(folder)' style="margin: 8px")
        q-avatar(icon="close" color="black" text-color="white" size='32px' )
    .col.column.fit
      .col(style='\
      display: flex;\
      flex-direction: column;\
      overflow-y: auto;\
      overflow-x: hidden;\
      background: #F2F3F5;\
      ')
        template(v-for='server in $store.state.serverlist', :key='server')
          emoticon-group-vue(:server='server')
      .col-shrink.q-pa-sm(style='background: #EBEDEF')
        div
          //- img(:src='`/statics/${selected_group}/${selected_emoticon}`', alt='', style='height: 32px; width: 32px')
        div
          div.text-bold {{ selected_emoticon }}
          div.text-caption from {{ selected_group }}


</template>

<script>
import emoticonGroupVue from "./emoticonGroup.vue";
import * as filelist_json from "./filelist.json";
export default {
  components: {
    emoticonGroupVue,
  },
  computed: {
    selected_emoticon() {
      return this.$store.state.selected_emoticon;
    },
    selected_group() {
      return this.$store.state.selected_group;
    },
    emoji_list() {
      return this.$store.state.serverdata.selected_serverdata.emoji
    }
  },
  methods: {
    scroll_into_view(folder) {
      console.log(folder);
      document.getElementById(folder).scrollIntoView(true);
    },
  },
  data() {
    return {
      folders: Object.keys(filelist_json.default),
      filelist_json: filelist_json,
      emoticon_category: 'emoji',
      emoticon_search: null,
    };
  },
};
</script>

<style>
.emoticon-container {
  height: 50vh;
  width: 40vw;
  border-radius: 5px;
}



</style>
