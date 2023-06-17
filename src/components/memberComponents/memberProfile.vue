<template lang="pug">
q-dialog(v-model="store_isvisible_profile" @before-hide="hide_modal")
	q-card( style="width:600px")
		q-img(src="~/assets/mountains.jpg" :ratio="16 / 4")
		q-card-section
			q-avatar(color="primary" icon="place" class="absolute avatar")
			div.absolute(style="right:15px")
				q-btn(color="green") Send friend request
		q-card-section
			div.text-h6 mccndcg
				span.text-grey #2134
		q-tabs(v-model="selected_tab")
			q-tab(name="user_info" label="User Info")
			q-tab(name="mutual_servers" label="Mutual Servers")
			q-tab(name="mutual_friends" label="Mutual Friends")
		q-tab-panels(v-model="selected_tab" animated)
			q-tab-panel(name="user_info")
				p USER INFO
			q-tab-panel(name="mutual_servers")
				p mutual_servers
			q-tab-panel(name="mutual_friends")
				p mutual_friends
</template>

<script>
export default {
	data() {
		return {
			selected_tab: 'user_info',
			isvisible_profile: this.store_isvisible_profile
		}
	},
	computed: {
		store_isvisible_profile() {
			return this.$store.state.isvisible_profile_modal
		}
	},
	methods: {
		hide_modal() {
			this.$store.commit('mutate_shallow', {'isvisible_profile_modal': false})
		}
	}
}
</script>

<style>

</style>