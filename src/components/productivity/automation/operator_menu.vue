<template lang="pug">
q-menu 
	template(v-if="['==', '>', '!='].includes(parent_operator)")
		q-item(clickable @click="$emit('set_type_value')") value
		q-item(clickable @click="$emit('set_type_object')") object
	q-item.text-grey-5 operator
	q-item(clickable @click="$emit('set_condition', 'or')") or
	q-item(clickable @click="set_condition('and')") and
	q-item(clickable @click="set_condition('==')") is
	q-item.text-grey-5 operator
	q-item(clickable @click="$emit('set_condition', '==')") ==
	q-item(clickable @click="set_condition('!=')") ==
	q-item(clickable @click="set_condition('gt')") gt
	q-item(clickable @click="set_condition('lt')") lt
	q-item(clickable @click="set_condition('gte')") gte
	q-item(clickable @click="set_condition('lte')") lte
</template>

<script>
export default {
	props: ["parent_operator"]
}
</script>

<style>

</style>