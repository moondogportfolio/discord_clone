<template lang="pug">
.q-pa-sm.thread-options
	q-input(outlined placeholder="New thread." label="Thread name" v-model="thread_name")
	q-select.q-mt-sm(outlined label="Archive after inactivity" :options="archive_time_options" v-model="archive_time")
	q-separator
	div.q-mt-sm.chat-single
		div
			q-avatar(size="42px")
				q-img(:src="`http://localhost:8000/user-icon/${post.author}`")
		div.q-mx-md(style="width: 100%")
			div.cursor-pointer.text-grey(v-if="post_reference") reply to: 
				span.reference-content(@click="scroll_to_reference") {{ post_reference.content }} {{ post.message_reference }}
			div
				div
					span.text-bold.q-mr-sm {{ post }}
					span {{ post.timestamp }}
				div.text-bold post_id: {{post_id}}
				div.text-bold post_thread: {{post.thread}}
				div(v-html="rendered()")
	q-btn.full-width.q-mt-sm(unelevated color="blue" @click="create_thread") Create thread
</template>

<script>
import chatSinglechat from "../chatComponents/chatSinglechat.vue";

export default {
	name: 'CreateThread',
	methods: {
		create_thread() {
			this.$store.commit('mutate_shallow', {
        thread_mode: 'loading'
        })
		},
		scroll_to_reference() {

		},
		rendered() {
      try {
        return this.$markdown.render(this.post.content);
      } catch (error) {
        return `cant be markdown rendered ${this.post.content}`
      }
    },
	},
	components: {
		chatSinglechat
		},
	computed: {
		post() {
			return this.$store.state.selected_post_object?.object
		},
		post_id() {
			return this.$store.state.selected_post_object?.id
		},
		post_reference() {
			return this.$store.state.selected_post_object?.reference
		}
	},
	data() {
		return {
			archive_time: null,
			thread_name: null,
			archive_time_options: ["1 Hour", "24 Hours", "3 Days", "1 Week"]
		}
	}
}
</script>

<style scoped>
.thread-options {
	position: absolute;
	bottom: 0;
	width: 100%;
}
</style>