<script lang="ts">
	import { draw } from 'svelte/transition';
	import * as d3 from 'd3';
	import { onMount } from 'svelte';

	//Props
  export let data: {year:number, index:number}[];
	export let width = 500;
	export let height = 300;

  console.log('Data changed?')
  console.log(data)

  const margin = ({top: 20, right: 30, bottom: 30, left: 40})

	let years: Number[] = data.length > 0 ? data.map((value) => value.year) : [0];
	let rainData = data.length > 0 ? data.map((value) => value.index) : [0];

	let xScale = d3
		.scaleLinear()
		.domain([d3.min(years) as number, d3.max(years) as number])
		.range([ margin.left,  width - margin.right]);

	let yScale = d3
		.scaleLinear()
		.domain([d3.min(rainData) as number, d3.max(rainData) as number])
		.range([height - margin.bottom, margin.top]);

	let line = d3
		.line<{ year: number; index: number }>()
		.x((d) => xScale(d.year))
		.y((d) => yScale(d.index));

	let xAxis = d3.axisBottom(xScale);
	let yAxis = d3.axisLeft(yScale);
  onMount(() => {
    d3.select('.x-axis')
      .call(xAxis);
    d3.select('.y-axis')
      .call(yAxis);
  });
</script>

<svg {width} {height}>
  <!-- <g class="x-axis" style="stroke-width:4">
    <svg:path d={xAxis}/>
  </g>
  <g class="y-axis" style="stroke-width:4">
    <svg:path d={yAxis}/>
  </g> -->
  {#if data.length > 0}
	  <path transition:draw={{ duration: 2000 }} d={line(data)}/>
  {/if}
</svg>

<style>
	path {
		stroke: black;
		stroke-width: 2;
		fill: none;
		stroke-linecap: round;
	}
</style>
