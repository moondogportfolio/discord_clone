<template lang="pug"> 
q-card
  q-card-section
    q-list
      q-item(
        clickable v-for="subfield in Object.entries(field)"
        :key="subfield[0]"
        @click="create_field(subfield[0])"
        )
        |	{{ subfield[1] }}
</template>

<script>
import { mapGetters } from 'vuex'
import { fields, constructor_dict } from '../../taskClasses/task_models.js'

export default {
  props: ['board_id'],
  created() {
    this.field = fields
  },
  computed: {
		...mapGetters(['selected_workspacedata', 'userstate']),
	},
  methods: {
    create_field(field_name) {
      
      if(['number', 'text', 'color', 'checkbox'].includes(field_name)) {
        var index
        var position = 0;
        if(_.has(this.selected_workspacedata.board[this.board_id], field_name)) {
          index = this.selected_workspacedata.field_meta[field_name].index
          this.$store.commit('mutate_set', {
            string: `workspacedata.${this.userstate.selected_workspace}.field_meta.${field_name}.index`,
            value: index + 1
          })
        }
        else {
          index = 0
          this.$store.commit('mutate_set', {
            string: `workspacedata.${this.userstate.selected_workspace}.field_meta.${field_name}.index`,
            value: 1
          })
        }
        
        let field_obj = constructor_dict[field_name](index, position)
        console.log(field_obj, index)
        // return
        this.$store.commit('mutate_set', {
          string: `workspacedata.${this.userstate.selected_workspace}.board.${this.board_id}.field.${field_name}.[${index}]`,
          value: field_obj
        })
      }
      else if(_.has(this.selected_workspacedata.field, field_name)) {
        return
      }
    }
  }
}
</script>

<style>

</style>