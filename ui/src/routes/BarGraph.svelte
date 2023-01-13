<script lang="ts">
  import { beforeUpdate, afterUpdate } from 'svelte';
  import * as d3 from "d3";

  export let width = 500;
	export let height = 300;

  export let data: {year:number, payout:number}[];

  const margin = ({top: 20, right: 30, bottom: 30, left: 40})

  beforeUpdate(()=>{
    d3.select("#bar-chart").html("");
  });

  afterUpdate(() => {
    const svg = d3.select("#bar-chart")
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    const xScale = d3.scaleBand()
      .domain(data.map(d => d.year))
      .range([ margin.left,  width - margin.right])
      .padding(0.1);

    const yScale = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.payout)])
      .range([height - margin.bottom, margin.top]);

    svg.selectAll("rect")
      .data(data)
      .enter()
      .append("rect")
      .attr("x", d => xScale(d.year))
      .attr("y", d => yScale(d.payout))
      .attr("width", xScale.bandwidth())
      .attr("height", d => height - yScale(d.payout))
      .attr("fill", "skyblue");

    // Need to fix this up so that it has the proper ticks
    // const xAxis = d3.axisBottom(xScale);
    // svg.append("g")
    //   .attr("transform", "translate(0,500)")
    //   .call(xAxis);

    // const yAxis = d3.axisLeft(yScale);
    // svg.append("g")
    //   .call(yAxis);
  });
</script>


{#if data.length > 0}
  <h2>Yearly Payout</h2>
  <div id="bar-chart"></div>
{/if}