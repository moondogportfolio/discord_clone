<template lang="pug">
div.automation-placeholder(v-if="condition && Object.keys(condition).length===0") logic
  operator-menu(
    :parent_operator="parent_operator"
    @set_type_value="set_type_value"
    @set_type_object="set_type_object"
    @set_condition="set_condition($event)"  
  )

div(v-else-if="condition==null || ['string', 'number'].includes(typeof(condition))")
  span.automation-value {{ condition || 'value' }}
    q-menu.row
      q-input.col(v-model="input_data")
      q-btn.col-shrink(unelevated @click="set_value") OK
div(v-else-if="Object.keys(condition)[0]=='var'")
  span.automation-value {{ condition?.var || 'var' }}
    attribute-menu(
      @set_attribute="set_attribute($event)"
    )
  //-   logic-menu(
  //-     @set_object="set_object($event)"
  //-   )
  //- span.automation-value {{ condition.value?.attribute || 'ATTRIBUTE' }}
div.row(v-else)
  div.col-shrink(style="width:40px")
    span.automation-variable {{ translation[operator] }}
      operator-menu(
        :parent_operator="parent_operator "
        @set_type_value="set_type_value"
        @set_type_object="set_type_object"
        @set_condition="set_condition($event)"
      )
  div.col.logic-block
    div(v-for="(sub_condition, index) in condition[operator]" :key="index")
      logic-circular(
        :condition="sub_condition"
        :depth="`${depth}.${operator}[${index}]`"
        :index="index"
        :parent_operator="operator"
      )
    div(style="opacity:0.2" @click="push_condition  ") Add new
</template>

<script>
import logicCircular from './logic';
import jsonLogic from 'json-logic-js';
import logicMenu from './object_menu.vue'
import operatorMenu from './operator_menu.vue'
import attributeMenu from './attribute_menu.vue'

var operators_list = [
  '>', '<', '==', '||', '&&', 'or', 'and'
]

export default {
  components: {
    logicMenu,
    operatorMenu,
    attributeMenu
  },
  name: 'logicCircular',
  props: ['condition', 'depth', 'parent_operator', 'index'],
  emits: ['set_value'],
  created() {
    if(this.condition!=null) {
      let operator = Object.keys(this.condition)[0]
      this.operator = operators_list.includes(operator) ? operator:null
    }
    this.translation = {
      'and': `&&`,
      'or': `||`,
      '==': `==`,
    }
  },
  data() {
    return {
      operator: null,
      input_data: null
    }
  },
  methods: {
    set_attribute(attribute) {
      this.$store.commit('mutate_logic_create', {
        path: `${this.depth}.var`,
        value: `task.${attribute}`
      })
    },
    set_value() {
      this.$store.commit('mutate_logic_create', {
        path: this.depth,
        value: this.input_data
      })
    },
    mutate_operator(operator) {
      this.$store.commit('mutate_logic_create', {
        path: this.depth,
        value: {[operator]: [{}]}
      })
    },
    set_object(object) {
      this.$store.commit('mutate_logic_create', {var: null})
    },
    set_type_value() {
      this.$store.commit('mutate_logic_create', {
        path: this.depth,
        value: null
      })
    },
    set_type_object() {
      
      console.log(this.depth);
      this.$store.commit('mutate_logic_create', {
        path: this.depth,
        value: {'type': 'object', 'value': {
          object: null,
          attribute: null
        }}
      })
    },
    set_condition(cond) {
      // eslint-disable-next-line vue/no-mutating-props
      // this.condition = {[cond]: [null, null, null]}
      // console.log(cond)
      this.operator = cond;
      this.$store.commit('mutate_logic_create', {
        path: this.depth,
        value: {[cond]: [{}, {}]}
      })
      // this.$emit('update:condition', {[cond]: [null, null, null]})
    },
  },

}
</script>

<style>
.sentence-filler {
  color: lightgrey;
}

.automation-value {
  border-bottom: 2px solid black;
  color: lightblue;
  width: fit-content;
  margin-right: 5px;
  cursor: pointer;
}

.automation-placeholder {
  /* min-width: 100px; */
  width: fit-content;
  border-bottom: 2px solid black;
  color: lightblue;
}

.automation-variable {
  border-bottom: 2px solid black;
  color: lightblue;
  cursor: pointer;
  font-family: monospace, Helvetica
}

.sentence {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
}

.logic-block {
  border-left: 1px solid black;
  padding-left: 5px;
}
</style>