<template lang="pug">
div.fixed-center
	q-card.invite-box.relative-position
		q-btn.switch(icon="close" round @click="isvalid_invite=!isvalid_invite")
		.column.items-center.q-pa-lg(v-if="isvalid_invite")
			q-avatar(icon="settings" color="black")
			.text-center {{inviter}} invited you to join
			div
				q-icon(name="settings" size="32px")
				span.text-h5 {{server_name}}
			div
				q-badge(rounded color="green")
				span.q-mr-md {{online}} online
				q-badge(rounded color="grey")
				span {{members}} online
			q-btn.full-width.q-mt-lg(unleveled color="blue") Accept Invite
		.column.items-center.q-pa-lg(v-else)
			div.text-h5 {{server_name}}
			div This link is expired.
			q-btn.full-width.q-mt-lg(unleveled color="blue") Continue to Discord
</template>

<script>
export default {
	name: 'invites',
	data() {
		return {
			inviter: 'mccndcg',
			server_name: 'mccndcgs server',
			online: 5,
			members: 6,
			isvalid_invite: true
		}
	}
}
</script>

<style scoped>
.invite-box {
    min-width: 30vw;
}

.switch {
	top: 0;
	right: 0;
	position: absolute;
	transform: translateY(-50%) translateX(50%);
}

</style>