<template lang="pug">
q-item.dm-item(@click="view_dm_room2(dm._id)" clickable)
	q-item-section(avatar)
		q-avatar(icon="settings")
	q-item-section
		q-item-label {{dm.name}}
		q-item-label(caption) {{ last_message }}
	q-item-section(side)
		q-icon(name="close")
		//- q-btn(:label="dm.name" @click="view_dm_room(dm._id)")
	q-menu(context-menu)
		q-list.shadow-6(separator)
			q-item(clickable @click="") Mark As Read
			q-item(clickable @click="") Change Icon
			q-item(clickable @click="") Invite to Server
				q-menu(anchor="top end" self="top start" )
					q-list.shadow-6(separator)
						q-item(clickable @click="") Server1
						q-item(clickable @click="") Server2
			q-item(clickable @click="") Leave Group
</template>

<script>
export default {
	props: ["dm"],
	computed: {
		last_message() {
			console.log(this.dm.posts)
			try {
				return Object.values(this.dm.posts)[Object.keys(this.dm.posts).length-1]?.content
			} catch (error) {
				return 'No message'
			}
		}
	},
	watch: {
		'dm.posts'(newval, oldval) {
			console.log(newval, oldval)
		}
	},
	methods: {
		view_dm_room2(dm_room_id) {
			this.$store.commit('mutate_deep', {
				focused_room: dm_room_id,
				selected_room: dm_room_id,
				userdata: {
					state: {
						selected_view: 'dm'
						}
					}
				}
				);
			console.log('TRANSFER VIEW')
			// console.log(this.$store.state.userdata.state.selected_room, this.$store.state.roomdata)
			this.$router.push(`/channels/@me/${dm_room_id}`);
			// console.log(this.$store.state.userdata.state.selected_dm)
		},
		view_dm_room(dm_room_id) {
			console.log(dm_room_id)
			this.$api({
				method: 'get',
				url: `/dm_room/${dm_room_id}`,
				headers : {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${this.$store.state.auth}`
				}
			}).then((response)=>{
				console.log("GET_CHANNEL_DM", response);
				this.$store.commit('mutate_deep', {userdata: {state: {selected_dm: dm_room_id, selected_view: 'dm'}}});
				this.$store.commit('mutate_shallow', {'roomdata': response.data})
				this.$router.push(`/channels/@me/${this.$store.state.userdata.state.selected_dm}`)
			}).catch((error) => {
				console.error(error)
			})
    },
	}
}
</script>

<style>

</style>