<template lang="pug">
p.text-h5 Server Members
q-list
	q-item 
		div {{member_count}} Members - 
			span.text-red.cursor-pointer Prune
	q-separator
	template(v-for="server_member in server_members" :key="server_members")
		q-item(clickable)
			q-item-section(avatar)
				q-avatar(color="black")
			q-item-section
				q-item-label {{server_member}}
				q-item-label a
			q-btn(icon="add")
			q-menu(touch-position)
				q-list.q-pa-sm
					q-item(clickable)
						q-item-section Invite people
						q-item-section(side)
							q-icon(name='settings' color="orange")
					q-item(clickable)
						q-item-section Server Settings
						q-item-section(side)
							q-icon(name='settings' color="green")

</template>

<script>
export default {
	computed: {
		server_members() {
			return this.$store.state.serverdata.selected_serverdata.members
		},
		member_count() {
			return Object.keys(this.$store.state.serverdata.selected_serverdata.members).length
		}
	}
}
</script>

<style>

</style>