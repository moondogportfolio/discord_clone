<template lang="pug">
q-card.q-pa-lg(style="width:90vw")
	q-card-section.automation-item
		div condition: AW
		div effect: AW

</template>

<script>
export default {

}
</script>

<style>
.automation-item:hover {
	box-shadow: 0 12px 24px 0 rgb(0 0 0 / 20%);
	transform: translate3d(0, -4px, 0);
}

.automation-item {
	transition: box-shadow .2s ease,transform .2s ease;
}
</style>