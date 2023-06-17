<template lang="pug">
q-virtual-scroll(
	:items="heavyList"
	separator
	)
	template(v-slot="{ item, index }")
		q-item.schedule-row(
			:key="index"
			)
			//- div.wrapper
			//- 	div.box(
			//- 		v-for="subitem in 16" :key="subitem"
			//- 		)
			div.bar.draggable(
				:id="`drag-0-${index}`"
				)
			div.bar.draggable(
				:id="`drag-1-${index}`"
				)
</template>


<script>
import interact from 'interactjs'
const maxSize = 10
const heavyList = []
import { debounce, throttle } from 'quasar'

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
	mounted() {

		var position = {
				x: 0,
				y: 0
			}
		var init_x = 0
		this.init_x = init_x
		

		var gridTarget = interact.snappers.grid({
		// can be a pair of x and y, left and top,
		// right and bottom, or width, and height
		
		y: 100,
		x: 100,

		// optional
		range: 10,

		// optional
		// offset: { x: 5, y: 10 },

		// optional
		// limits: {
		// 	top: 0,
		// 	left: 0,
		// 	bottom: 500,
		// 	height: 500
		// }
		})
		heavyList.forEach((ele, index)=>{ [0,1].forEach(inner_index=>{
			console.log(index)
			var position = {
				x: 0,
				y: 0
			}
			interact(`#drag-${inner_index}-${index}`).resizable({
				// resize from all edges and corners
				edges: { left: true, right: true, bottom: true, top: false },

				listeners: {
				move (event) {
					var target = event.target
					var x = (parseFloat(target.getAttribute('data-x')) || 0)
					var y = (parseFloat(target.getAttribute('data-y')) || 0)

					// update the element's style
					target.style.width = event.rect.width + 'px'
					target.style.height = event.rect.height + 'px'

					// translate when resizing from top or left edges
					if(event.deltaRect.right > 0 || event.deltaRect.right < 0) {
						console.log(event.dx)
						position.x += event.dx
						target.style.transform = 'translate(' + position.x + 'px)'
						console.log(event.dx)
					}


					target.setAttribute('data-x', x)
					target.setAttribute('data-y', y)
					target.textContent = Math.round(event.rect.width) + '\u00D7' + Math.round(event.rect.height)
				}
				},
				modifiers: [
				// keep the edges inside the parent
				interact.modifiers.restrictEdges({
					outer: 'parent'
				}),

				// minimum size
				interact.modifiers.restrictSize({
					min: { width: 100, height: 30 }
				})
				],

				inertia: true
			}).draggable({
					
				startAxis: 'xy',
				lockAxis: 'x',
				modifiers: [
					interact.modifiers.restrictEdges({
						outer: 'parent'
					}),
					interact.modifiers.snap({
						targets: [
						interact.snappers.grid({ x: 100, y: 100 })
						],
						range: Infinity,
						relativePoints: [ { x: 0, y: 0 } ]
					}),
				],
				listeners: {
					start (event) {
					console.log(event, event.target)
					},
					move (event) {
					console.log(event, event.target)


					// var x = (parseFloat(event.target.getAttribute('data-x')) || 0)
					// var y = (parseFloat(event.target.getAttribute('data-y')) || 0)
					
					position.x += event.dx

					// event.target.setAttribute('data-x', position.x)
					// event.target.setAttribute('data-y', position.y)

					event.target.style.transform =
						`translate(${position.x}px)`
					},
				}
			})
		})
		})
	},
	data() {
		return {
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
	/* gap: 2px; */
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

.schedule-row {
	background-image:
      repeating-linear-gradient(#ccc 0 1px, transparent 1px 100%),
      repeating-linear-gradient(90deg, #ccc 0 1px, transparent 1px 100%);
    background-size: 10000px 300px;
	height:300px;
	padding: 0 !important;
}

.q-list--separator > .q-virtual-scroll__content > .q-item-type + .q-item-type {
	border-top: 0 !important;
}
</style>