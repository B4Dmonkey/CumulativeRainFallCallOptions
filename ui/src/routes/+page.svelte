<script lang="ts">
  import Controls from './Controls.svelte';
  import Stats from './Stats.svelte';
  import Table from './Table.svelte';
	import LineGraph from './LineGraph.svelte';
	import BarGraph from './BarGraph.svelte';
  import { optionType } from "./store"
</script>

<div id="app" class="h-screen grid grid-cols-1 gap-10">
  <!-- Inputs -->
  <div>
  <!-- <div> -->
    <Controls />
  </div>
  <!-- Results -->
  <div class="grid grid-cols-3 justify-items-center">
    <!-- Line Graph -->
    <div>
      <h1>Line Graph</h1>
      <!-- <LineGraph/> -->
    </div>
    <!-- Bar Graph -->
    <div>
      <h1>Bar Graph</h1>
      <!-- <BarGraph/> -->
    </div>
    <!-- Summary -->
    <div>
      <Stats/>
    </div>
  </div>
  <!-- Full Results -->
  <div>
    <!-- <h1>Table</h1> -->
    <Table/>
  </div>
</div>
