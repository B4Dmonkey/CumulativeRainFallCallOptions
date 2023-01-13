<script lang="ts">
  import * as d3 from 'd3';

  export let data: {year:number, payout:number}[];
  export let width = 500;
  export let height = 300;
  const margin = ({top: 20, right: 30, bottom: 30, left: 40})

</script>

<svg {width} {height}>
  {#if data.length > 0}
    <path />
  {/if}
</svg>
