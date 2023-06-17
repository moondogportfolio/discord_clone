<template lang="pug">
.thread-mini.q-pa-sm(@click="$emit('show_thread')")
	div.text-bold 
		span.text-bold.q-mr-sm Thread title
		span.text-blue.thread-link 32 Messages
	div.thread-mini-details
		q-icon(name="settings" size="16px")
		//- q-avatar(size="42px")
		//- 	q-img(:src="`http://localhost:8000/user-icon/${post.author}`")
		div.ellipsis Rendered text. Rendered text. Rendered text. Rendered text. Rendered text. Rendered text. Rendered text. 
		span.text-grey 1min ago.
</template>

<script>
export default {
	methods: {
		
	}
}
</script>

<style>
.thread-mini {
	background: lightgray;
	border-radius: 5px;
	width: 45vw;
	cursor: pointer;
}

.thread-mini:hover .thread-link {
	text-decoration: underline;
}

.thread-mini-details {
	display: flex;
	flex-wrap: nowrap;
	white-space: nowrap;
}

</style>