<template lang="pug">
q-table.main-table(:rows="rows" :columns="columns" row-key="id")
  template(v-slot:header="props")
    q-tr
      q-th(v-for="col in props.cols" :key="col.fieldname")
        | {{ col.label }}
  template(v-slot:body="props")
    q-tr
      template(v-for="col in props.cols" :key="col.fieldname")
        q-td.text-grey.table-cell 
          span(v-if="col.fieldname=='resource'") {{ resources?.[props.row?.[col.fieldname]]?.name }}
          span(v-else) {{ props.row?.[col.fieldname] }}
          q-menu
            menu-input(
              v-if="col.fieldname == 'amount'"
              type="number"
              :value="props.row?.[col.fieldname]"
              @update_cell="update_cell($event, props.row.index, 'amount')"
            )
            menu-option(
              v-else-if="col.fieldname == 'resource'"
              :options="resources"
              @update_cell="update_cell($event, props.row.index, 'resource')"
            )
            menu-date(
              v-else-if="col.fieldname == 'transfer_date'"
              :value="props.row?.[col.fieldname]"
              type="date"
            )
            menu-select(
              v-else-if="col.fieldname == 'entity'"
              :options="options"
              @emit_value="update_cell($event, props.row.index, 'entity')"
            )
  template(v-slot:bottom-row="props")
    q-tr
      q-td( colspan="100%")
        q-input(
          outlined
          dense
          placeholder="Add resource amount"
          v-model="input_amount"
          @keyup.enter="add_transaction_item"
          autofocus
          )
          template(v-slot:append)
            q-btn(icon="add" dense flat @click="add_transaction_item")
</template>

<script>
import menuInput from '../../productivity/taskComponents/main table/menu-input.vue'
import menuOption from '../../productivity/taskComponents/main table/menu-option.vue'
import menuDate from '../../productivity/taskComponents/main table/menu-daterange.vue'
import menuSelect from '../../productivity/taskComponents/main table/menu-select.vue'


export default {
  props: ['resources', 'rows'],
	components: {
		menuInput,
    menuOption,
    menuDate,
    menuSelect
	},
  methods: {
    update_cell(value,row, fieldname) {
      this.$emit('update_cell',{
        value: value,
        row: row,
        field: fieldname
      })
    },
    add_transaction_item() {
      this.$emit('add_transaction_item', this.input_amount)
      this.input_amount = null;
    }
  },
  data() {
		return {
      input_amount: null,
      options:[
				'Google', 'Facebook', 'Twitter', 'Apple', 'Oracle'
			],
			columns: [
				{label: 'Amount', fieldname: 'amount'},
				{label: 'Resource', fieldname: 'resource'},
				{label: 'Transfer Date', fieldname: 'transfer_date'},
        {label: 'Entity', fieldname: 'entity'}
				],
		}
	}

}
</script>

<style>

</style>


class InvolvedResource(BaseModel):
    amount: int
    internal_id: Optional[ObjectIdStr]
    description: Optional[str]
    transfer_date: Optional[datetime] #no transfer_date assumes transfer is same as tx date
