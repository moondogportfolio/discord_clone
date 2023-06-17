<template lang="pug">
q-menu(anchor="top end" self="top start" )
	q-item(clickable @click="$emit('set_object', 'created_task')") created task
	q-item(clickable @click="$emit('set_object', 'deleted_task')") deleted task
	q-item(clickable @click="$emit('set_object', 'modified_task')") modified task
	q-item(clickable @click="$emit('set_object', 'moved_task')") moved task
	q-item(clickable @click="$emit('set_object', 'date')") date
	q-item(clickable @click="$emit('set_object', 'task_metadata')") task metadata
</template>

<script>
export default {

}
</script>

<style>

</style>