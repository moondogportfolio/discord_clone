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
import AppearanceVue from './Appearance.vue'
import ChangelogVue from './Changelog.vue'
import KeybindsVue from './Keybinds.vue'
import myAccountVue from './myAccount.vue'
import NotificationsVue from './Notifications.vue'
import PrivacyAndSafetyVue from './Privacy and Safety.vue'
import TextAndImagesVue from './Text and Images.vue'
import UserProfileVue from './User Profile.vue'




var settings_dict = {
	'My Account': {
		name: 'My Account',
		component: myAccountVue,
	},
	'UserProfile': {
		name: 'UserProfile',
		component: UserProfileVue,
	},
	'Appearance': {
		name: 'Appearance',
		component: AppearanceVue,
	},
	// 'Privacy and Safety': {
	// 	name: 'Privacy and Safety',
	// 	component: PrivacyAndSafetyVue,
	// },
	// 'Text and Images': {
	// 	name: 'Text and Images',
	// 	component: TextAndImagesVue,
	// },
	// 'Notifications': {
	// 	name: 'Notifications',
	// 	component: NotificationsVue,
	// },
	// 'Keybinds': {
	// 	name: 'Keybinds',
	// 	component: KeybindsVue,
	// },
	Changelog: {
		name: 'Changelog',
		component: ChangelogVue,
	},
}


export default {
	name: 'settingsContainer',
	created() {
		this.settings = settings_dict
	},
	computed: {
		selected_setting_component() {
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
			selected_setting_component_key: 'My Account'
		}
	}
}
</script>

<style scoped>
.settings-left {
	background: #2F3136;
	color: white;
}

.close-btn {
	position: fixed;
	top: 15px;
	right: 15px;
}
</style>