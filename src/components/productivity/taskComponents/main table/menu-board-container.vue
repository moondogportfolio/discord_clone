<template lang="pug">
div.row(style="gap:5px; align-items: center;").q-ma-sm
	q-btn.col-shrink(icon="expand_more" dense rounded flat)
		q-menu.table-menu
			menu-board(
        @add_task_dialog="$emit('add_task_dialog')"
        :board_id="board_id"
        )
			
	div.col.text-h5 Main Board
</template>

<script>
import menuCreateField from './menu-create-field.vue'
import menuBoard from './menu-board.vue'
export default {
	props: ['board_id'],
	emits: ['add_task_dialog'],
	components: {
		menuCreateField,
		menuBoard
	}
}
</script>

<style>

</style>