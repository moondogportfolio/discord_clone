<template lang="pug">
q-list(dense)
	q-item(clickable @click="show_profile_modal")
		q-item-section Profile
	q-item(clickable)
		q-item-section Mention
	q-separator
	q-item(clickable)
		q-item-section Message
	q-item(clickable)
		q-item-section Call
	q-item(clickable)
		q-item-section Add Note
	q-separator
	q-item(clickable)
		q-item-section Mute
		q-item-section(side)
			q-checkbox(v-model="ismuted")
	q-item(clickable)
		q-item-section Change Nickname
	q-item(clickable)
		q-item-section Remove Friend
	q-item(clickable)
		q-item-section Block
	q-separator
	q-item(clickable)
		q-item-section.text-red Kick Jaja
	q-item(clickable)
		q-item-section.text-red Ban Jaja


</template>

<script>
export default {
	data() {
		return {
			ismuted: false,
		}
	},
	methods: {
		show_profile_modal() {
			this.$store.commit('mutate_shallow', {'isvisible_profile_modal': true})
		}
	}
}
</script>

<style>

</style>