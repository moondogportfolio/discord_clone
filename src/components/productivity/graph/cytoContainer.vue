<template lang="pug">
#cyto
div {{ selected_workspacedata.board['6129fe58ffb50fb57a849a6f'].task }}
div {{ edges }}
div {{ node_serializer }}
q-btn(@click="wenk") ok
</template>

<script>
import { mapGetters } from 'vuex';
const cyjson = require("./init.json");
var cytoscape = require("cytoscape");


export default {
	mounted() {
		cyjson.container = document.getElementById("cyto");
		var cy = cytoscape(cyjson);
		// this.add_cytograph(cy);
		cy.add(this.node_serializer)
		cy.add(this.edges)
		this.cy=cy
		console.log(cy.data())
	},
	methods: {
		wenk() {
			let options = {
					"name": "breadthfirst",
					"directed": true,
					"fit": true
			}
			this.cy.elements().layout(options).run()
		}
	},
	data() {
		return {
			edges: [],
			cy: null
		}
	},
	computed: {
		...mapGetters(['selected_workspacedata']),
		node_serializer() {
			return Object.entries(this.selected_workspacedata.board['6129fe58ffb50fb57a849a6f'].task).map(task=>{
				task[1].completion_dependency.ends_with_required.forEach(dependency=>this.edges.push({
					data: {
						id: dependency+task[0],
						source: task[0],
						target: dependency,
						group: 'edges'
					}
				}))
				console.log(task[0])
				return {
					data: {
						id: task[0],
						position: {x:0, y: 0},
						group: 'nodes'
					}
				}
			})
		}
	}
}
</script>

<style>
#cyto{
	height: 40vh;
  border: 1px solid black;
}

</style>