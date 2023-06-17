<template lang="pug">
q-virtual-scroll(
	:items="heavyList"
	separator
	)
	template(v-slot="{ item, index }")
		q-item(
			:key="index"
			dense
			)
			div.wrapper
				div.box(
					v-for="subitem in 16" :key="subitem"
					)
				div.bar(
					:id="`drag-${index}`"
					draggable="true"
					@mousedown="click_event"
					@mousemove="mouse_move"
					@drag="drag_bar"
					@dragstart="drag_start"
					@dragend="drag_end"
					@mouseleave="mouse_leave"
					)
</template>


<script>
const maxSize = 10
const heavyList = []
import { debounce } from 'quasar'

for (let i = 0; i < maxSize; i++) {
heavyList.push({
	label: 'Option ' + (i + 1)
})
}


export default {
	methods: {
		click_event(event) {
			console.log(event.x, event.y, event.target.getBoundingClientRect())
			let dimensions = event.target.getBoundingClientRect()
			if((event.x >= dimensions.x && event.x <= dimensions.x+5) || (
				event.x <= dimensions.right && event.x >= dimensions.right-5)) {
					this.drag_mode = 'resize'
					this.init_x = dimensions.x + dimensions.width
					event.target.classList.add('resize-drag')
				}
			else {
				this.delta_x = event.x - dimensions.x
				this.drag_mode = 'move'
			}
			
		}
	},
	created() {
		this.drag_bar = _.throttle((event)=>{
			console.log('is_dragging')
			console.log(event)
			if(this.drag_mode == 'resize') {
				event.target.style.width = `${this.init_x - event.pageX -8}px`;
				event.target.style.left = `${event.pageX -8}px`;
			}
			else {
				event.target.style.left = `${event.pageX - this.delta_x - 12}px`;
			}
			}, 50)
		this.drag_over = _.throttle((event)=>{
			return
			event.target.classList.add('drop-over')
			console.log('enter drag over')
			},100)
		this.drag_start = _.throttle((event)=>{
			var img = new Image();
			img.src = 'data:image/gif;base64,R0lGODlhAQABAIAAAAUEBAAAACwAAAAAAQABAAACAkQBADs=';
			event.dataTransfer.setDragImage(img, 0, 0);
			this.is_dragging = true;
			return

			},100)
		this.drag_leave = _.throttle((event)=>{
			return 
			},100)
		this.drag_end = _.throttle((event)=>{
			console.log('drag_end')
			this.is_dragging = false;
			return 
			},100)
		this.mouse_move = _.throttle((event)=> {
			if(this.is_dragging) return
			let dimensions = event.target.getBoundingClientRect()
			if((event.x >= dimensions.x && event.x <= dimensions.x+5) || (
				event.x <= dimensions.right && event.x >= dimensions.right-5)
				) {
				event.target.classList.add('resize-drag')
				this.drag_mode = 'resize'
			}
			else {
				event.target.classList.remove('resize-drag')
				this.drag_mode = 'move'
			}
		},100)
		this.mouse_leave = _.throttle((event)=> {
			event.target.classList.remove('resize-drag')
		})
	},
	data() {
		return {
			init_x: 0,
			drag_mode: null,
			is_dragging: false,
			delta_x: 0

		}
	},
	setup () {
		return {
			heavyList
		}
	}
}
</script>
<style>
.wrapper {
	display: grid;
	grid-template-columns: repeat(16, 1fr);
	gap: 2px;
	width:100%;
	position: relative;
}

.resize-drag:hover {
	cursor:ew-resize;
}

.bar {
	height: 30px;
	width: 100px;
	border: 1px solid cornflowerblue;
	background:beige;
	position:absolute;
	top:10px;
	right: 20px;
}

.connector-left {
	width: 20px;
	background:orange;
	border: black;
	height: 6px;
	content:"";
	position: absolute;
	left: -21px;
	top:12px;
}

.connector-point-right {
	height: 15px;
	width: 15px;
	background: lightgreen;
	border-radius: 10px;
	position: absolute;
	right: -21px;
	transform: translate(3px, 30%)
}

.connector-point-right:hover {
	cursor: pointer;
}

.connector-point-left {
	height: 15px;
	width: 15px;
	background: lightgreen;
	border-radius: 10px;
	position: absolute;
	left: -21px;
	transform: translate(-3px, 30%)
}

.connector-point-left:hover {
	cursor: pointer;
}


.connector-right {
	width: 20px;
	background:orange;
	height: 6px;
	content:"";
	position: absolute;
	right: -21px;
	top:12px;
}

.box {
	border: 1px solid bisque;
	height: 50px;
	width: 100%;
}

.drop-leave {
	background: lightgreen;
}

.drop-over {
	background: lightgrey;
}
</style>