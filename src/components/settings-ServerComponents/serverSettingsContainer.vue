<template lang="pug">
div.row
	div.col-2.settings-left
		q-list.q-ma-md
			q-item(
				v-for="setting_component in settings"
				:key="setting_component"
				clickable
				@click="setting_goto(setting_component.name)")
				q-item-section {{setting_component.name}}
	div.col.q-pa-md
		component(:is="selected_setting_component")
		q-btn.close-btn(round icon="close" @click="mutate_settings_overlay")
	div.col-1
</template>

<script>
import AuditLogVue from './AuditLog.vue'
import EmojiVue from './Emoji.vue'
import InvitesVue from './Invites.vue'
import MembersVue from './Members.vue'
import OverviewVue from './Overview.vue'
import RolesVue from './Roles.vue'



var settings_dict = {
	'AuditLog': {
		name: 'AuditLog',
		component: AuditLogVue,
	},
	'Emoji': {
		name: 'Emoji',
		component: EmojiVue,
	},
	'Invites': {
		name: 'Invites',
		component: InvitesVue,
	},
	'Members': {
		name: 'Members',
		component: MembersVue,
	},
	'Overview': {
		name: 'Overview',
		component: OverviewVue,
	},
	Roles: {
		name: 'Roles',
		component: RolesVue,
	},
}

export default {
    name: 'SettingsContainer',
    created() {
		this.settings = settings_dict
	},
	computed: {
		selected_setting_component() {
			console.log(this.settings, this.selected_setting_component_key)
			return this.settings[this.selected_setting_component_key].component;
		}
	},
	methods: {
		setting_goto(component_name) {
			this.selected_setting_component_key = component_name
		},
		mutate_settings_overlay() {
			this.$store.commit('mutate_shallow', {settings_overlay: false})
		},
	},
	data() {
		return {
			selected_setting_component_key: 'Overview'
		}
	}
}
</script>

<style>
.settings-left {
	background: #2F3136;
	color: white;
}

.close-btn {
	position: fixed;
	top: 15px;
	right: 15px;
}

/* .q-focus-helper {
	border-radius: 5px !important;
} */
</style>