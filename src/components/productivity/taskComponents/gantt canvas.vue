<template lang="pug">
q-btn(@click="draw") OK
//- .canvas-wrapper
	//- canvas#canvas(style='width:900px; height: 400px;')
#div_template
</template>

<script>
import * as d3 from 'd3';
export default {
	props: ["rows"],
	mounted() {
		var margin = {top: 20, right: 25, bottom: 30, left: 40},
			width = 450 - margin.left - margin.right,
			height = 450 - margin.top - margin.bottom;

		// append the svg object to the body of the page
		var svg = d3.select("#div_template")
		.append("svg")
			.attr("width", width + margin.left + margin.right)
			.attr("height", height + margin.top + margin.bottom)
		// .append("g")
		//   .attr("transform",
		//         "translate(" + margin.left + "," + margin.top + ")");
		console.log(this.rows)
		// add the squares
		svg.selectAll()
			.data(this.rows)
			.enter()
				.append("text")
					.text(d => d.name)
					.attr("x", 10)
					.attr("y", (d, i) => (i * 10 * 2.25)+ 40)
				.insert("text")
					.text(d => d['date-start'])
					.attr("x", 80)
					.attr("y", (d, i) => (i * 10 * 1.25)+ 40)
				.append('g')
				.insert("rect")
					.attr("x", 40)
					.attr("y", (d, i) => (i * 10 * 1.25)+ 40)
					.attr("rx", 4)
					.attr("ry", 4)
					.attr("width", 10)
					.attr("height",  10)
					.style("stroke-width", 4)
					.style("stroke", "none")
					.style("opacity", 0.8)

	},
	methods: {
		draw() {
			var ctx = document.getElementById('canvas').getContext('2d');
			ctx.font = '48px serif';
			ctx.textBaseline = "hanging";
			ctx.fillText('Hello world', 10, 0);
		}
	},
}
</script>

<style>

#canvas {
  border: 1px solid black;
}

/* .canvas-wrapper {
	overflow: scroll;
} */
</style>