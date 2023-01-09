<script lang="ts">

	import { draw } from 'svelte/transition';
	
	import { extent } from 'd3-array';
	import { scaleLinear } from 'd3-scale';
	import { line, curveBasis } from 'd3-shape';

	// props
	export let data: Array<object>;
  export let show: Boolean;

  //Graph Dimensions
  let el;
  let width = 800;
	let height = 300;
	let margin = { top: 20, bottom: 20, left: 20, right: 20 };

  // d's for axis paths
	let xPath = `M${margin.left + .5},6V0H${width - margin.right + 1}V6`
	let yPath = `M-6,${height + .5}H0.5V0.5H-6`
	
	// scales
	const xScale = scaleLinear()
		.domain(extent(data.map(d => d.age)))
		.range([5, 95]);
	
	const yScale = scaleLinear()
		.domain(extent(data.map(d => d.temp)))
		.range([5, 75]);
	
	// the path generator
	const pathLine = line()
		.x(d => xScale(d.age))
		.y(d => yScale(d.temp))
		.curve(curveBasis);
</script>

{#if (show)}
  <!-- <svg viewBox="0 0 100 100"> -->
  <svg bind:this={el} transform="translate({margin.left}, {margin.top})">
      <!-- Line Data -->
      <g>
        <path 
          transition:draw={{duration: 2000}}
          d={pathLine(data)} 
        />
      </g>

      <!-- X Axis -->
      <g transform="translate(0, {height})">
        <!-- "M 20.5, 6 V0 H781 V6" -->
        <!-- Move to a point draw a vertical line draw a horizontal line draw a vertical line -->
        <path stroke="currentColor" d="{xPath}" fill="none" />
      </g>
      
      <!-- y axis -->
      <g transform="translate({margin.left}, 0)">
        <path stroke="currentColor" d="{yPath}" fill="none" />
      </g>
  </svg>
{/if}

<style>
  svg {
		width: 100%;
		height: 100%;
	}
	.tick {
		font-size: 11px;
	}
	path {
		stroke: black;
		stroke-width: 2;
		fill: none;
		stroke-linecap: round;
	}
</style>