<template lang="pug">

q-item.user-card
  q-item-section(avatar)
    q-avatar(size="34px")
      img(src="~/assets/new_logo.jpg")
      q-badge(rounded, color="red", floating) 
  q-item-section
    q-item-label mccndcg
    q-item-label(caption) #5773
  q-item-section(side)
    div
      q-btn(flat padding="xs" color="black" icon="settings" @click="show_settings")


//- div.container
//-   q-card(flat square)
//-     q-card-section.items-center.q-py-sm(style="background-color: #ebedef")
//-       q-avatar.q-ma-xs(size="34px")
//-         img(src="~/assets/new_logo.jpg")
//-       div.row.items-center.full-width
//-         div.col
//-           div.col.text-bold.q-pb-none mccndcg
//-           div.col.text-caption #5773
//-         div.col-shrink
//-           q-btn(flat padding="xs" color="red" icon="favorite")
//-           q-btn(flat padding="xs" color="red" icon="favorite")
//-           q-btn(flat padding="xs" color="red" icon="settings" @click="show_settings")

  //- <div class="container">
  //-   <q-card flat square>
  //-     <q-card-section
  //-       horizontal
  //-       class="items-center q-py-sm"
  //-       style="background-color: #ebedef"
  //-     >
  //-       <q-avatar size="34px" class="q-ma-xs">
  //-         <img src="~/assets/new_logo.jpg" />
  //-       </q-avatar>
  //-       <div class="row items-center full-width">
  //-         <div class="col">
  //-           <div class="col text-bold q-pb-none">Mccndcg</div>
  //-           <div class="col text-caption">#5773</div>
  //-         </div>
  //-         <div class="col-shrink">
  //-           <q-btn flat padding="xs" color="red" icon="favorite" />
  //-           <q-btn flat padding="xs" color="accent" icon="bookmark" />
  //-           <q-btn flat padding="xs" color="red" icon="favorite" />
  //-         </div>
  //-       </div>
  //-     </q-card-section>
  //-   </q-card>
  //- </div>
</template>

<script>
export default {
  name: "channelCard",
  methods: {
    show_settings() {
      this.$store.commit('mutate_shallow', {settings_overlay: true})
    }
  }
};
</script>

<style scoped>
.user-card {
  background: snow;
}
</style>
