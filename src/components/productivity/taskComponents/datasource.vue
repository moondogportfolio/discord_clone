<template lang="pug">
main-table(
  :items="items"
  :rows="rows"
  :columns="columns"
  :fields="fields"
  @update_cell="update_cell($event)"
  @create_task="create_task"
  @create_field="create_field($event)"
  )

kanban(
  v-if="false"
  :rows="rows"
  :columns="columns"
  :items="items"
)

gantt-canvas(
  v-if="false"
  :rows="rows"
)

	
</template>

<script>
import mainTable from './main table/maintable.vue'
import kanban from './kanban/kanban.vue'
import ganttCanvas from './gantt canvas.vue'


var items = {
  'name': {
    label: 'Name',
    default: 'Default name'
  },
  'number': {
    label: 'Number',
    default: 0
  },
  'people': {
    label: 'People',
    default: 'Test guy'
  },
  'status': {
    label: 'Status',
    default: 'Doing',
    options: {
      'Stuck': {
        color: 'red'
      } ,
      'Done': {
        color: 'green'
      },
      'Doing': {
        color: 'orange'
      },
      'To-do': {
        color: 'yellow'
      }
    }
  },
  'color-picker': {
    label: 'Color picker',
    default: '#ffffff'
  },
  'date-start': {
    label: 'Start',
    type: 'date-picker',
    default: '1/1/2020'
  },
  'date-end': {
    label: 'End',
    type: 'date-picker',
    default: '1/1/2020'
  },
  'starts-with': {
    label: 'Starts With',
    type: 'date-picker',
  },
  'ends-with': {
    label: 'Ends With',
    type: 'date-picker',
  },
  'end-awaits-start-of': {
    label: 'Unendable until',
    type: 'date-picker',
  },
  'start-awaits-end-of': {
    label: 'Ends With',
    type: 'date-picker',
  },
  
}

export default {
  components: {
    mainTable,
    kanban,
    ganttCanvas
  },
  created() {
    this.items = items
  },
  methods: {
    update_cell({row, col, input,}) {
      console.log(row, col, input)
      this.rows[row][col] = input;
    },
    create_task() {
      this.rows = this.rows.concat(
        this.columns.reduce((prev, cur) => {prev[cur.field] = this.items[cur.field].default; return prev}, {})
      )
    },
    create_field(item) {
      console.log(item)
      let fieldname = item[0]
      if(this.fields?.[fieldname]) {
        this.fields[fieldname] += 1
        fieldname = `${fieldname}${this.fields?.[fieldname]-1}`
      }
      else {
        this.fields[fieldname] = 1
      }
      this.rows = this.rows.map(ele => {
        ele[fieldname] = 'TEST'
        return ele
      })
      this.columns = this.columns.concat({
        label: `${item[1].label} ${fieldname.slice(item[0].length)}`,
        field: fieldname,
        type: item[1]?.type ? item[1].type : item[0] 
      })
    }
  },
  data() {
    return {
      input_val: null,
      fields: { "name": 1, "date-start": 1, "date-end": 1, number: 1, "status": 1},
      columns: [
        { "label": "Name ", "field": "name", "type": "name" },
        { "label": "Status ", "field": "status", "type": "status" },
        { "label": "Start ", "field": "date-start", "type": "date-picker" },
        { "label": "End ", "field": "date-end", "type": "date-picker" },
        { "label": "Number ", "field": "number", "type": "number" },
        ],
      rows: [
        { "name": "TEST", "status": "To-do", "date-start": "2021/08/27", "date-end": "2021/08/29", number: 1 },
        { "name": "TEST", "status": "Done", "date-start": "2021/08/24", "date-end": "2021/08/31", number: 1 },
        { "name": "TEST", "status": "Stuck","date-start": "2021/08/11", "date-end": "2021/08/28", number: 1 },

        ]
    };
  },
};
</script>

<style>
</style>