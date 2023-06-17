<template lang="pug">
div.column.main.window-height
	div.col
		div(v-for="command in commands" :key="command") {{ command }}
	div.col-shrink
		q-input(autofocus v-model="input" dark borderless @keyup.enter="enter_command")
</template>

<script>
export default {
	methods: {
		enter_command() {
			this.commands.push(this.input);
			this.input = null;
		}
	},
	data() {
		return {
			input: null,
			commands: []
		}
	}
}
</script>

<style>
.main {
	background: black;
	color: white;
}
</style>