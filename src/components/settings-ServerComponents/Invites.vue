<template lang="pug">

p.text-h5 Invites
p Here's a list of all active invite links. You can revoke any one.
q-table(:rows="invites" :columns="columns" row-key="invite_code")
</template>

<script>
export default {
	computed: {
		invites() {
			return Object.entries(this.$store.getters.selected_serverdata.invites).map(
				ele => {
					return ele[1]
				}
			)
		}
	},
	data() {
		return {
			columns: [
					{ name: 'invite_code', align: 'center', label: 'Invite Code', field: 'calories'},
					{ name: 'room', label: 'Room', field: 'room' },
					{ name: 'inviter', align: 'center', label: 'Inviter', field: 'inviter'},
					{ name: 'max_age', label: 'Max Age', field: max_age => max_age['weeks']},
					{ name: 'temporary', label: 'Temporary', field: 'temporary' },
					{ name: 'expires_at', label: 'Expiry', field: 'expires_at' },
					{ name: 'uses', label: 'Uses', field: 'uses' },
				]
		}
	}
}
</script>

<style>

</style>
