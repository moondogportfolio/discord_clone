<template lang="pug">
q-card.absolute-center(style="width: 30vw; height:80vh")
  q-card-section.q-pa-none
    q-tabs.col-shrink(
      v-model="tab"
      class="text-grey"
      active-color="primary"
      inline-label
      indicator-color="primary"
      align="justify"
      narrow-indicator
    )
      q-tab(name="settings" label="Field Settings")
      q-tab(name="attributes" label="Field Attributes")
    q-separator
    q-tab-panels.col(v-model="tab")
      q-tab-panel(name="settings")
        q-item
          q-item-section(side)  
            q-btn(icon="add")
          q-item-section
            q-input(label="Add new" standout)
              template(v-slot:append)
                q-icon(style="background:red; height:40px; width:40px")
            
        q-item(v-for="item in 5" :key="item") 
          q-item-section(side)
            q-checkbox
          q-item-section Status
          q-item-section(side)
            div(style="background:red; height:40px; width:40px")
      q-tab-panel(name="attributes")
        q-item(v-for="item in 15" :key="item")
          q-item-section
            q-item-label Length
          q-item-section(side)
            q-item-label 15

</template>

<script>
export default {
  data() {
    return {
      tab: 'settings',
      model: 'one'
    }
  }
}
</script>

<style>

</style>