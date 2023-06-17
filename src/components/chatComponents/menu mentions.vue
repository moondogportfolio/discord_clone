<template lang="pug">
q-list.q-mb-sm
	q-item(clickable v-for="mention in mentions" :key="mention" @click="parse_mention(mention)")
		q-item-section(avatar)
			q-icon(name="settings")
			q-item-section
				q-item-label {{ mention }}
			//- q-item-section
			//-   q-item-label {{ command }}
			q-item-section(side)
				q-item-label Application Test
</template>

<script>


export default {
	props: ["offset"],
	data() {
		return {
			isvisible_mentionmenu: true,
			userlist: ['jajarrrr', 'jajaxasdasd', 'jaja', 'jajas', 'testest', 'testra'],
			user_partial: null,
			message_shards: null,
			mention_node: null,
			mention_text: null
		}
	},
	methods: {
		parse_mention(mention) {
      let before_ele = null
      let after_ele = null

			

			console.log(this.mention_text, this.message_shards)

      if(this.mention_text.slice(0, this.message_shards[1]).length > 0) {
        before_ele = document.createElement('span')
        const before_ele_text = document.createTextNode(this.mention_text.slice(0, this.message_shards[1]))
        before_ele.appendChild(before_ele_text)
      }

      const middle_ele = document.createElement('span')
      const middle_ele_text = document.createTextNode(`${mention}----`)
      middle_ele.setAttribute('contenteditable', 'false')
      middle_ele.appendChild(middle_ele_text)
      middle_ele.className = 'mention'

      if(this.mention_text.slice(this.message_shards[2]).length > 0) {
        after_ele = document.createElement('span')
        const after_ele_text = document.createTextNode(this.mention_text.slice(this.message_shards[2], ))
        after_ele.appendChild(after_ele_text)
      }
			
			if(this.mention_node.id == 'contenteditable') {
				this.mention_node.textContent = null
				this.mention_node.append(...[before_ele, middle_ele, after_ele].filter(ele=>ele!=null))
			}
			else {
	      this.mention_node.replaceWith(...[before_ele, middle_ele, after_ele].filter(ele=>ele!=null))
				this.user_partial = null
			}
			this.user_partial = null
		}
	},
	computed: {
		mentions() {
			return (
				this.user_partial ?
				this.userlist.filter(ele => this.user_partial == ele.slice(0, this.user_partial.length)) : []
				)
		}
	},
	watch: {
    offset(newval, oldval) {
      // https://javascript.plainenglish.io/how-to-find-the-caret-inside-a-contenteditable-element-955a5ad9bf81
      this.mention_text = window.getSelection().baseNode.data
      this.mention_node = window.getSelection().baseNode.parentNode
      if(this.mention_text==null || !this.mention_node.isContentEditable ) return
      let offset = newval
      let re = /(?<=^|\s)@\w*/g
      let message_shards = [...this.mention_text.matchAll(re)].map(ele => [ele[0],ele.index,ele.index+ele[0].length])
        .find(ele => offset > ele[1] && offset <= ele[2])
 			this.user_partial = message_shards? message_shards[0].slice(1,) : null
			this.message_shards = message_shards
    }
  },
}
</script>

<style>
.mentions-menu {
	height: 30vh;
	border: 1px solid black;
}
</style>