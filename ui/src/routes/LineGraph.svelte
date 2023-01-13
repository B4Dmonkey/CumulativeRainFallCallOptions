<script lang="ts">
	import { draw } from 'svelte/transition';
	import * as d3 from 'd3';
	import { beforeUpdate, afterUpdate } from 'svelte';
  // import {data } from './store'

	//Props
  export let data: {year:number, index:number}[];
	export let width = 500;
	export let height = 300;

  const margin = ({top: 20, right: 30, bottom: 30, left: 40})

	let years: Number[] = data.length > 0 ? data.map((value) => value.year) : [];
	let rainData: Number[] = data.length > 0 ? data.map((value) => value.index) : [];

  console.log('data is')
  console.dir(data.length)
  console.log('Years is')
  console.dir(years)
  console.log('Rain Data is')
  console.dir(rainData)
  let xScale;
  let yScale;
  let line;

  beforeUpdate(() => {
    xScale = d3
      .scaleLinear()
      .domain([d3.min(years) as number, d3.max(years) as number])
      .range([ margin.left,  width - margin.right]);

    yScale = d3
      .scaleLinear()
      .domain([d3.min(rainData) as number, d3.max(rainData) as number])
      .range([height - margin.bottom, margin.top]);

    line = d3
      .line<{ year: number; index: number }>()
      .x((d) => xScale(d.year))
      .y((d) => yScale(d.index));

    let xAxis = d3.axisBottom(xScale);
    let yAxis = d3.axisLeft(yScale);
  
    d3.select('.x-axis')
      .call(xAxis);
    d3.select('.y-axis')
      .call(yAxis);
  });

  // beforeUpdate, afterUpdate
</script>

{#if data.length > 0}
  <h2>Rain Fall Index</h2>
  <h2>Data is {data}</h2>
  <h3>Line is {line(data)}</h3>
{/if}
<svg {width} {height}>
  <!-- <g class="x-axis" style="stroke-width:4">
    <svg:path d={xAxis}/>
  </g>
  <g class="y-axis" style="stroke-width:4">
    <svg:path d={yAxis}/>
  </g> -->
  <!-- {@debug data} -->
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
