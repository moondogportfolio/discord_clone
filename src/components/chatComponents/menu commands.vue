<template lang="pug">
div {{input_chat}}
div {{ subcommands }}
q-list.q-mb-sm(bordered v-if="iscasting_command!==null && iscasting_command.length>0")
  q-item(clickable v-for="command in iscasting_command" :key="command.name")
    q-item-section
      q-item-label {{ command.name }}
        template(v-if="command.options !== null")
          q-badge.q-ml-sm(v-for="option in command.options.filter(ele=>ele.name!=null)" :key="option.name" color='grey') {{option.name}}
      q-item-label(caption) {{ command.description }}
    //- q-item-section
    //-   q-item-label {{ command }}
    q-item-section(side)
      q-item-label Application Test
div.chat-input-wrapper.q-ma-sm
  q-item(v-if="selected_command!=null")
    q-item-section
      q-item-label {{ selected_command.name }}
        template(v-if="selected_command.options !== null")
            template(v-for="(option, index) in selected_command.options.filter(ele=>ele.name!=null)" :key="option.name") 
              q-badge.q-ml-sm.cursor-pointer(
                :color="selected_option == index? 'green': 'gray'"
                ) {{option.required? null:'OPTIONAL'}} {{option.name}}
      //- q-item-label(caption v-if="selected_option == -1") {{ selected_command.description }}
      //- q-item-label(caption v-else-if="selected_command.options.length-1 >= selected_option") {{ selected_command.options[selected_option].description }}
    q-item-section(side)
      q-item-label Application Test
</template>

<script>
export default {
	props: ["input_chat"],
	data() {
		return {
			subcommands: null,
      selected_command: null,
      selectedStart: 0,
		}
	},
  
	computed: {
		iscasting_command() {
      try {
        if(this.input_chat[0]=='/') {
          return this.$store.state.applist.filter(ele=>`${this.input_chat}`==`/${ele.name.slice(0,this.input_chat.length-1)}`)
        }
        return null
      }
      catch(error) {
        return null
      } 
    },
		selected_option() {
      var accumulator = this.selected_command.name.length+1
      if(this.selectedStart < accumulator ) return -1
      let re = /^\/\w+\s$/
      if(re.test(this.input_chat)) return 0
      return this.subcommands.findIndex(ele=> {
        accumulator += ele.length+1;
        console.log(this.selectedStart, accumulator)
        return this.selectedStart <= accumulator
        });
    },
	},
  watch: {
    input_chat(newval, oldval) {
      this.selectedStart = document.querySelector('.chat-input').selectionStart
      if(this.input_chat==null || this.input_chat[0]!='/') {
        this.selected_command = null;
        return
      }
      var command_finder = /(^\/\w+\s)(.*)/g
      var subcommand_finder = /\w+/g
      this.selected_command = this.$store.state.applist.find(
        ele => {
          if(this.input_chat.slice(0, ele.name.length+2) == `/${ele.name} `) {
            // this.subcommands = [...[...this.input_chat.matchAll(command_finder)][0][2].matchAll(subcommand_finder)];
            this.subcommands = [...this.input_chat.matchAll(command_finder)][0][2].match(subcommand_finder);

            return true
            
          };
        }
      )
    }
  },
}
</script>

<style>

</style>